from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass


class AddStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a + b


class MultiplyStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a * b


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_work(self, a: int, b: int) -> int:
        return self._strategy.execute(a, b)


if __name__ == "__main__":
    ctx = Context(AddStrategy())
    print("Add:", ctx.do_work(2, 3))

    ctx.set_strategy(MultiplyStrategy())
    print("Multiply:", ctx.do_work(2, 3))
