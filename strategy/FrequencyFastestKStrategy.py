from strategy.Strategy import Strategy
from utils.CollectionUtils import CollectionUtils


class FrequencyFastestKStrategy(Strategy):

    def __init__(self, top_k_value=1):
        self.top_k_value = top_k_value

    def get_top_data_providers(self, frames):
        output_dict = dict()
        for (_, seq_entries) in self.create_seq_to_source_mapping(frames).items():
            sorted_list_for_segno = CollectionUtils.sort_tuple_by_values(seq_entries)

            for item in sorted_list_for_segno[:self.top_k_value]:
                source = item[0]
                if source not in output_dict:
                    output_dict[source] = 0
                output_dict[source] += 1

        return output_dict

    def get_top_n_data_providers(self, frames, n):
        outputs = self.get_top_data_providers(frames)
        sorted_outputs = CollectionUtils.sort_tuple_by_values(outputs)
        return sorted_outputs[:n]

    def get_name(self):
        return "Frequency of Fastest-Top-K {} Sources\n".format(self.top_k_value)

    def __str__(self):
        return self.get_name()
