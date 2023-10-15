from __future__ import annotations

from typing import List, Any
from collections.abc import Iterator, Iterable


class MyIterator(Iterator):
    def __init__(self, iterable: MyCollection):
        self._iterable = iterable
        self._position = 0

    def __next__(self):
        try:
            value = self._iterable.collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration

        return value


class MyCollection(Iterable):
    def __init__(self, collection: List[Any]):
        self.collection = collection

    def __iter__(self) -> MyIterator:
        return MyIterator(self)
