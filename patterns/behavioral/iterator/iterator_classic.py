from __future__ import annotations

from typing import List
from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass


class Iterable(ABC):
    @abstractmethod
    def get_iterator(self) -> Iterator:
        pass


class MyNumberCollection(Iterable):
    def __init__(self, collection: List[str]):
        self._collection = collection

    def get_iterator(self) -> NumberIterator:
        return MyNumberCollection.NumberIterator(self)

    class NumberIterator(Iterator):
        def __init__(self, outer_class: MyNumberCollection):
            self.outer_class = outer_class
            self._index = 0

        def has_next(self) -> bool:
            return True if self._index < len(self.outer_class._collection) else False

        def next(self) -> str:
            value = self.outer_class._collection[self._index]
            self._index += 1
            return value
