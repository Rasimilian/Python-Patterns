from typing import TypeVar

from patterns.structural.adapter.base_objects import Russian, American


class MestizoInheritance(Russian, American):
    """Adapter implementation via inheritance."""

    def __init__(self):
        super().__init__()

    def speak(self) -> None:
        self.speak_english()


class MestizoComposition(Russian):
    """Adapter implementation via composition and inheritance partially."""

    def __init__(self, american: American):
        super().__init__()
        self.american = american

    def speak(self) -> None:
        self.american.speak_english()


Russian_ = TypeVar("Russian_", bound=Russian)


def client_code(russian: Russian_) -> None:
    russian.speak()
