from __future__ import annotations

import random
from typing import List
from abc import ABC, abstractmethod


class AbstractWorker(ABC):
    def __init__(self, blackboard: Blackboard) -> None:
        self.blackboard = blackboard

    @abstractmethod
    def is_ready(self):
        pass

    @abstractmethod
    def contribute(self):
        pass


class SimpleWorker(AbstractWorker):
    def is_ready(self) -> bool:
        return True

    def contribute(self) -> None:
        self.blackboard.progress += 1
        self.blackboard.contributors.append(self.__class__.__name__)


class HardWorker(AbstractWorker):
    def is_ready(self) -> bool:
        return bool(random.randint(0, 1))

    def contribute(self) -> None:
        self.blackboard.progress += random.randint(1, 5)
        self.blackboard.contributors.append(self.__class__.__name__)


class Blackboard:
    def __init__(self, progress_limit: int) -> None:
        self.progress_limit = progress_limit
        self.workers = []
        self.progress = 0
        self.contributors = []

    def add_worker(self, worker: AbstractWorker) -> None:
        self.workers.append(worker)


class Controller:
    def __init__(self, blackboard: Blackboard) -> None:
        self.blackboard = blackboard

    def run(self) -> List[str]:
        while self.blackboard.progress < self.blackboard.progress_limit:
            for worker in self.blackboard.workers:
                if worker.is_ready():
                    worker.contribute()
        return self.blackboard.contributors
