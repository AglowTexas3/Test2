from collections.abc import Iterator


class EvenNumbers:
    def __init__(self, limit: int) -> None:
        self._limit = limit

    def __iter__(self) -> Iterator[int]:
        return EvenIterator(self._limit)


class EvenIterator(Iterator[int]):
    def __init__(self, limit: int) -> None:
        self._limit = limit
        self._current = 0

    def __next__(self) -> int:
        self._current += 2
        if self._current > self._limit:
            raise StopIteration
        return self._current


if __name__ == "__main__":
    for n in EvenNumbers(10):
        print(n)
