from strategy.Strategy import Strategy
from utils.CollectionUtils import CollectionUtils


class AverageTimeStrategy(Strategy):

    def __init__(self):
        pass

    def get_top_data_providers(self, frames):
        output_dict = dict()
        source_to_times_mapping = AverageTimeStrategy.create_source_to_time_mapping(frames)
        for (source, times) in source_to_times_mapping.items():
            output_dict[source] = sum(times) / float(len(times))

        return output_dict

    def get_top_n_data_providers(self, frames, n):
        outputs = self.get_top_data_providers(frames)
        sorted_outputs = CollectionUtils.sort_map_by_values(outputs)
        return sorted_outputs[:n]

    @staticmethod
    def get_name():
        return "Mean of Sources\n"

    def __str__(self):
        return self.get_name()
