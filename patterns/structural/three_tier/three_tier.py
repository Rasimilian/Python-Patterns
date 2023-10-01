from typing import Dict, List


class Data:
    """Data tier"""

    @staticmethod
    def get_from_database() -> Dict[str, Dict[str, int]]:
        objects = {
            "object1": {"id": 1},
            "object2": {"id": 2},
            "object3": {"id": 3}
        }
        return objects


class ApplicationLogic:
    """Application tier"""

    def __init__(self):
        self.data = Data.get_from_database()

    def object_list(self) -> List[str]:
        return list(self.data.keys())

    def find_object_by_id(self, object_id: int) -> str:
        for obj, obj_data in self.data.items():
            if obj_data["id"] == object_id:
                return obj
        else:
            raise ValueError(f"No object with ID: {object_id}!")


class UI:
    """User interface tier"""

    def __init__(self):
        self.app_logic = ApplicationLogic()

    def show_objects(self):
        for obj in self.app_logic.object_list():
            print(f"There is {obj} in the system.")

    def show_object_by_id(self, ids: List[int]):
        for id_ in ids:
            obj = self.app_logic.find_object_by_id(id_)
            print(f"There is {obj} with ID {id_} in the system.")
