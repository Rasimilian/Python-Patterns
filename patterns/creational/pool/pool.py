from __future__ import annotations
from queue import Queue
from threading import Lock


class CostlyResource:
    """An object with costly initialization which is better to keep in memory than recreate."""

    _value = None

    def __init__(self):
        pass

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value

    def reset(self):
        """Reset configuration"""
        self._value = None


class ObjectPool:
    """Object pool should be a singleton."""

    _instance: ObjectPool = None
    _lock: Lock = Lock()
    _resources = None

    def __new__(cls, *args, **kwargs) -> ObjectPool:
        """Singleton behavior."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._resources = Queue(maxsize=kwargs["size"])
        return cls._instance

    def get_item(self, block: bool = True, timeout: float = None):
        if self._resources.empty():
            print("New object has been created.")
            return CostlyResource()
        else:
            return self._resources.get(block, timeout)

    def put_item(self, item: CostlyResource, block: bool = True, timeout: float = None):
        if self._resources.full():
            print("Queue is full...")
        item.reset()
        self._resources.put(item, block, timeout)

    def size(self):
        return self._resources.qsize()
