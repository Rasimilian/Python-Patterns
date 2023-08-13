from __future__ import annotations
from threading import Lock


class Singleton:
    """
    Classical implementation of Singleton.
    """
    _lock: Lock = Lock()
    _instance: Singleton = None
    value: str = None

    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls, value: str) -> Singleton:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print('Creating new instance')
                    cls._instance = cls.__new__(cls)
                    cls._instance.value = value
        return cls._instance
