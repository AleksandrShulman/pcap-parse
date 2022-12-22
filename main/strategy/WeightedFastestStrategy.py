from main.strategy.Strategy import Strategy
from main.strategy.utils.CollectionUtils import CollectionUtils


class WeightedFastestStrategy(Strategy):

    def get_name(self):
        return "Frequency of Weighted Fastest Sources\n"

    def get_top_data_providers(self, frames):
        output_dict = dict()
        for (_, seq_entries) in self.create_seq_to_source_mapping(frames).items():
            sorted_list_for_segno = CollectionUtils.sort_tuple_by_values(seq_entries)

            rank = 0
            for item in sorted_list_for_segno:
                source = item[0]
                amount_to_award = self._get_points_to_award(rank, len(sorted_list_for_segno))
                if source not in output_dict:
                    output_dict[source] = amount_to_award
                output_dict[source] += amount_to_award
                rank += 1

        return output_dict

    def get_top_n_data_providers(self, frames, n):
        outputs = self.get_top_data_providers(frames)
        sorted_outputs = CollectionUtils.sort_tuple_by_values(outputs)
        return sorted_outputs[:n]

    @staticmethod
    def _get_points_to_award(rank, total_sources):
        # Accentuate frequent best and worst performers
        points = total_sources - rank
        if rank == 0:
            points += 15
        elif rank == (total_sources - 1):
            points -= 15

        return points

    def __str__(self):
        return self.get_name()
