from strategy import AverageTimeStrategy
from strategy import FrequencyFastestKStrategy
from strategy import Strategy
from strategy import WeightedFastestStrategy


class StrategyMap:
    id_to_strategy_template = {
        1: AverageTimeStrategy,
        2: FrequencyFastestKStrategy,
        3: WeightedFastestStrategy
    }

    def __init__(self, k=1):
        self.id_to_strategy = {
            1: AverageTimeStrategy.AverageTimeStrategy(),
            2: FrequencyFastestKStrategy.FrequencyFastestKStrategy(k),
            3: WeightedFastestStrategy.WeightedFastestStrategy()
        }

    def get_strategy(self, strategy_id) -> Strategy:
        return self.id_to_strategy[strategy_id]

    def __str__(self):
        output = """
        Strategy to execute:
        [DEFAULT] Run all strategies: 0 [recommended because it\'s awesome :)]
        """
        output += "\n"
        for (sid, strategy) in self.id_to_strategy.items():
            output += "\n{}: {}".format(sid, strategy)

        return output

    @staticmethod
    def default_help():
        output = """
                Strategy to execute:
                [DEFAULT] Run all strategies: 0 [recommended because it\'s awesome :)]
                """
        output += "\n"
        for (sid, strategy) in StrategyMap.id_to_strategy_template.items():
            output += "\n{}: {}".format(sid, strategy)

        return output