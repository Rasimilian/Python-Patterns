from typing import List, TypeVar
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def cancel(self):
        pass


Command_ = TypeVar("Command_", bound=Command)


class ShowGraphCommand(Command):
    def execute(self):
        print("Showing a graph")

    def cancel(self):
        print("Clearing a graph")


class UpdateDataCommand(Command):
    def execute(self):
        print("Updating data")

    def cancel(self):
        print("Restoring data")


class UndoCommand(Command):
    history: List[Command_] = list()

    def execute(self):
        try:
            command = self.history.pop()
            command.cancel()
        except IndexError:
            pass

    def cancel(self):
        pass


class Invoker:
    def __init__(self, command: Command_):
        self._command = command

    def on_do_button(self):
        self._command.execute()
        if not isinstance(self._command, UndoCommand):
            UndoCommand.history.append(self._command)
