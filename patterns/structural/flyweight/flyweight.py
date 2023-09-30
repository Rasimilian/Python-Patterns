from typing import Dict, List, Tuple, Union


class Smartphone:
    """The Flyweight"""

    def __init__(self, shared_manufacturer: str, shared_model: str):
        self._shared_manufacturer = shared_manufacturer
        self._shared_model = shared_model

    def make_call(self):
        print(f"Making call from the smartphone {self._shared_manufacturer} {self._shared_model}")


class SmartphoneMarket:
    _smartphones: Dict[str, Smartphone] = {}

    def __init__(self, smartphone_info: List[Union[List[str], Tuple[str, ...]]]):
        for info in smartphone_info:
            self._smartphones[SmartphoneMarket.smartphone_unique_id(info[0], info[1])] = \
                Smartphone(shared_manufacturer=info[0],
                           shared_model=info[1])

    @staticmethod
    def smartphone_unique_id(manufacturer: str, model: str) -> str:
        return manufacturer + "_" + model

    def get_smartphone(self, smartphone_info) -> Smartphone:
        smartphone_unique_id = SmartphoneMarket.smartphone_unique_id(smartphone_info[0], smartphone_info[1])

        if not self._smartphones.get(smartphone_unique_id):
            print(f"Added new smartphone to the cache: {smartphone_unique_id}")
            self._smartphones[smartphone_unique_id] = Smartphone(shared_manufacturer=smartphone_info[0],
                                                                 shared_model=smartphone_info[1])
        else:
            print(f"Reused cached smartphone: {smartphone_unique_id}")

        return self._smartphones[smartphone_unique_id]

    def list_cached_smartphones(self) -> int:
        return len(self._smartphones)
