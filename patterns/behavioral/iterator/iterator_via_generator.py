from typing import Generator


def numbers_up_to(number: int) -> Generator[str, int, None]:
    numbers = ["one", "two", "three", "four", "five"]
    yield from numbers[:number]
