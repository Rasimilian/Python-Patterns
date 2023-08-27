from __future__ import annotations
from typing import List, Any
import copy


class PrototypeContainer:
    def __init__(self):
        self.prototypes: List[Prototype] = []

    def add_prototype(self, prototype: Prototype):
        self.prototypes.append(prototype)


class Prototype:
    def __init__(self, value: Any, list_of_objects: List[Any], container: PrototypeContainer):
        self.value = value
        self.list_of_objects = list_of_objects
        self.container = container

    def copy(self) -> Prototype:
        """Returns a shallow copy of the Prototype as the copy.copy() method"""

        list_of_objects = copy.copy(self.list_of_objects)
        container = copy.copy(self.container)

        obj = self.__class__(self.value, list_of_objects, container)
        # Updates class fields to have true refs to the original ones or
        # if some fields were added by monkey-patching (not via __init__)
        obj.__dict__.update(self.__dict__)

        return obj

    def deepcopy(self, memo=None) -> Prototype:
        """Returns a deep copy of the Prototype as the copy.deepcopy() method"""
        if memo is None:
            memo = {}

        list_of_objects = copy.deepcopy(self.list_of_objects, memo)
        container = copy.deepcopy(self.container, memo)

        obj = self.__class__(self.value, list_of_objects, container)
        obj.__dict__ = copy.deepcopy(self.__dict__, memo)

        return obj
