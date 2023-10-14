from __future__ import annotations

from abc import ABC, abstractmethod


class Priority:
    INFO: int = 1
    WARNING: int = 2
    CRITICAL: int = 3


class Handler(ABC):
    _next_handler: Handler = None

    def __init__(self, priority: int):
        self.priority = priority

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def notify(self, request: str):
        pass

    def handle(self, request: str, priority: int):
        if priority <= self.priority:
            self.notify(request)
        else:
            if self._next_handler:
                self._next_handler.handle(request, priority)


class Assistant(Handler):
    def notify(self, request: str):
        print(f"Assistant handles the request: {request}")


class Manager(Handler):
    def notify(self, request: str):
        print(f"Manager handles the request: {request}")


class SeniorManager(Handler):
    def notify(self, request: str):
        print(f"Senior manager handles the request: {request}")
