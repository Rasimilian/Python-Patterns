from typing import List
from copy import deepcopy
from datetime import datetime


class Memento:
    def __init__(self, state: dict):
        self._state = deepcopy(state)

    def get_state(self) -> dict:
        return self._state


class Project:
    def __init__(self, name: str, cost: int):
        self._name = name
        self._cost = cost

    def add_expenses(self, amount: int):
        self._cost += amount

    def change_project_name(self, name: str):
        self._name = name

    def save(self):
        return Memento(self.__dict__)

    def restore(self, memento: Memento):
        self.__dict__.clear()
        self.__dict__.update(memento.get_state())


class Repository:
    def __init__(self, project: Project):
        self._mementos: List[Memento] = []
        self._project = project

    def backup(self):
        self._mementos.append(self._project.save())

    def undo(self):
        try:
            memento = self._mementos.pop()
            self._project.restore(memento)
        except IndexError:
            pass

    def get_project_state(self) -> dict:
        return self._project.__dict__
