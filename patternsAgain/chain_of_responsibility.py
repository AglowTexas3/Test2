from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    def __init__(self, successor: Optional["Handler"] = None) -> None:
        self._successor = successor

    def set_successor(self, successor: "Handler") -> None:
        self._successor = successor

    def handle(self, request: int) -> None:
        handled = self._handle(request)
        if not handled and self._successor:
            self._successor.handle(request)

    @abstractmethod
    def _handle(self, request: int) -> bool:
        pass


class SmallNumberHandler(Handler):
    def _handle(self, request: int) -> bool:
        if request < 10:
            print(f"SmallNumberHandler обработал {request}")
            return True
        return False


class MediumNumberHandler(Handler):
    def _handle(self, request: int) -> bool:
        if 10 <= request < 100:
            print(f"MediumNumberHandler обработал {request}")
            return True
        return False


class DefaultHandler(Handler):
    def _handle(self, request: int) -> bool:
        print(f"DefaultHandler получил {request}, но не знает, что делать")
        return True


if __name__ == "__main__":
    chain = SmallNumberHandler(MediumNumberHandler(DefaultHandler()))
    for number in [3, 25, 200]:
        chain.handle(number)
