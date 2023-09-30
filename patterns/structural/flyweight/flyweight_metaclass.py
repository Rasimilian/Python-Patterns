from __future__ import annotations
from weakref import WeakValueDictionary


class SmartphoneMeta(type):
    def __new__(mcs, cls, parents, dct):
        dct["pool"] = WeakValueDictionary()
        return super().__new__(mcs, cls, parents, dct)

    @staticmethod
    def _smartphone_unique_id(manufacturer: str, model: str) -> str:
        # unique_id = list(map(str, args))
        # unique_id.extend([str(kwargs), cls.__name__])
        # unique_id = "_".join(unique_id)
        return manufacturer + "_" + model

    def __call__(cls, manufacturer: str, model: str, *args, **kwargs) -> SmartphoneM:
        unique_id = SmartphoneMeta._smartphone_unique_id(manufacturer, model)
        pool = getattr(cls, "pool", {})

        instance = pool.get(unique_id)
        if instance is None:
            print(f"Added new smartphone to the cache: {unique_id}")
            instance = super().__call__(manufacturer, model, *args, **kwargs)
            instance._manufacturer = manufacturer
            instance._model = model
            pool[unique_id] = instance
        else:
            print(f"Reused cached smartphone: {unique_id}")
        return instance


class SmartphoneM(metaclass=SmartphoneMeta):
    def __init__(self, *args, **kwargs):
        self._manufacturer = None
        self._model = None

    def make_call(self):
        print(f"Making call from the smartphone {self._manufacturer} {self._model}")

    @staticmethod
    def list_cached_smartphones() -> int:
        return len(SmartphoneM.pool)
