from typing import TypeVar
from abc import ABC, abstractmethod


class Maker(ABC):
    @abstractmethod
    def make(self) -> None:
        pass


class MoneyMaker(Maker):
    def make(self) -> None:
        print("Making money...")


class IdeaMaker(Maker):
    def make(self) -> None:
        print("Making ideas...")


Maker_ = TypeVar("Maker_", bound=Maker)


class Organization(ABC):
    def __init__(self, maker: Maker_):
        self.maker = maker

    @abstractmethod
    def operate(self) -> None:
        pass


class Institute(Organization):
    def operate(self) -> None:
        print("Institute is working now...")
        self.maker.make()


class Company(Organization):
    def operate(self) -> None:
        print("Company is working now...")
        self.maker.make()
