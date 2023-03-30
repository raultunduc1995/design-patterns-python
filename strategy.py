from abc import ABC, abstractmethod


class FilterStrategy(ABC):

    @abstractmethod
    def remove_value(self, value):
        pass


class RemoveNegativeStrategy(FilterStrategy):

    def remove_value(self, value):
        return value < 0


class RemoveOddStrategy(FilterStrategy):

    def remove_value(self, value):
        return abs(value) % 2


class Values:

    def __init__(self, values) -> None:
        self.values = values

    def filter(self, strategy):
        result = []
        for number in self.values:
            if not strategy.remove_value(number):
                result.append(number)
        return result


if __name__ == '__main__':
    exampleValues = Values([-7, -4, -1, 0, 2, 6, 9])
    print(f'Remove negative values: {exampleValues.filter(RemoveNegativeStrategy())}')  # [0, 2,6, 9]
    print(f'Remove odd values: {exampleValues.filter(RemoveOddStrategy())}')  # [-4, 0, 2, 6]
