from __future__ import annotations
from threading import Lock


class Singleton:
    """
    Pythonic implementation of Singleton.
    """
    _instance: Singleton = None
    _lock: Lock = Lock()
    value: str = None

    def __new__(cls, *args, **kwargs) -> Singleton:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print('Creating new instance')
                    cls._instance = super().__new__(cls)
                    cls._instance.value = args[0]
        return cls._instance
