from weakref import WeakValueDictionary


class Smartphone:
    """The Flyweight"""

    _pool: WeakValueDictionary = WeakValueDictionary()

    def __new__(cls, manufacturer: str, model: str, *args, **kwargs):
        smartphone_unique_id = Smartphone.smartphone_unique_id(manufacturer, model)
        obj = cls._pool.get(smartphone_unique_id)
        if obj is None:
            print(f"Added new smartphone to the cache: {smartphone_unique_id}")
            obj = object.__new__(Smartphone)
            cls._pool[smartphone_unique_id] = obj
            obj._shared_manufacturer, obj._shared_model = manufacturer, model
        else:
            print(f"Reused cached smartphone: {smartphone_unique_id}")
        return obj

    @staticmethod
    def smartphone_unique_id(manufacturer: str, model: str) -> str:
        return manufacturer + "_" + model

    def make_call(self):
        print(f"Making call from the smartphone {self._shared_manufacturer} {self._shared_model}")

    @staticmethod
    def list_cached_smartphones() -> int:
        return len(Smartphone._pool)
