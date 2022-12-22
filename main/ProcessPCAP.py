import argparse
import json
import pathlib

from main.strategy.Strategy import Strategy
from main.strategy.StrategyMap import StrategyMap


class ProcessPCAC:

    # TODO: make this pluggable with a function to get json from a file path
    def __init__(self, strategy: Strategy, input_path, output_path, force_overwrite=False):
        if not pathlib.Path.exists(input_path):
            raise Exception("Bad path {}".format(input_path))

        if not pathlib.Path.exists(output_path) or force_overwrite:
            ProcessPCAC.extract_pcac_to_json_file(input_path, output_path)

        self.frames = ProcessPCAC.get_frames(output_path)
        self.strategy = strategy

    def get_best_n_providers(self, n=2):
        return self.strategy.get_top_n_data_providers(n)

    def describe_best_n_provider(self, n=2):
        results = self.strategy.get_top_n_data_providers(self.frames, n)
        print("For strategy {} top results were:\n {}".format(self.strategy.get_name(), results))

    @staticmethod
    def get_frames(filename):
        with open(filename, "r") as f:
            frames = json.load(f)

        return frames

    @staticmethod
    def extract_pcac_to_json_file(input_path, output_path):
        from pcapkit import extract
        extract(fin=input_path,
                fout=output_path,
                format='json',
                extension=False)


def parse():
    parser = argparse.ArgumentParser(
        usage="python ProcessPCAP.py -i <pcap_file_path> -o <json_output_file_path> -n <num_best> -s <strategy>",
        description='Run a test of lowest-latency input sources given a strategy'
    )

    parser.add_argument('-i', '--input', action='store', type=str, required=False,
                        default=get_default_input_path(),
                        help='Path to the input PCAP file. By default will use bundled sample file.')
    parser.add_argument('-o', '--output', action='store', type=str, required=False,
                        default=get_default_output_path(),
                        help='Path to the output of parsing the PCAP file into json. '
                             'By default will use pre-processed file.')
    parser.add_argument('-n', '--num-best', action='store', type=int, required=False,
                        default=2,
                        help='The number of top sources to report. All other sources omitted.')
    parser.add_argument('-k', '--k-top-candidates', action='store', type=int, required=False,
                        default=1,
                        help='Only for FrequencyFastestKStrategy: Number of top candidates considered ')
    parser.add_argument('-s', '--strategy', action='store', type=int, required=False,
                        default=0,
                        help=StrategyMap().__str__())

    return parser.parse_args()


def get_default_input_path():
    resource_path = pathlib.Path.cwd() / "../resources"
    return resource_path / "feed_arbitrage.pcap"


def get_default_output_path():
    resource_path = pathlib.Path.cwd() / "../resources"
    return resource_path / "parsed_pcap.json"


def execute_strategy(strategy: Strategy, input, output, num_best=2):
    p = ProcessPCAC(strategy, input, output)
    p.describe_best_n_provider(num_best)


if __name__ == "__main__":
    args = parse()
    sm = StrategyMap(args.k_top_candidates)

    if args.strategy != 0:
        strategy = sm.get_strategy(args.s)

        print("Executing single strategy {} to produce top {} sources".format(strategy, args.num_best))
        execute_strategy(strategy, args.input, args.output, args.num_best)
    else:
        print("Executing all strategies to produce top {} sources:".format(args.num_best))
        for strategy in sm.id_to_strategy.values():
            execute_strategy(strategy, args.input, args.output, args.num_best)
