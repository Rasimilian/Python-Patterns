from typing import Any, Dict
from threading import Lock, Thread


class SingletonMeta(type):
    """
    Thread-safe implementation of Singleton.
    """
    _instances = {}
    _locks: Dict[Any, Lock] = {}

    def __call__(cls, *args, **kwargs):
        # Initialization of the Singleton class blocks access for other threads until
        # the original thread has completed.
        if cls not in cls._instances:
            if cls not in cls._locks:
                cls._locks[cls] = Lock()
            with cls._locks[cls]:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value
