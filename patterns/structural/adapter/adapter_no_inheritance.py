from typing import Callable, TypeVar, Union

from patterns.structural.adapter.base_objects import Russian, American, Chinese

Nationality = TypeVar("Nationality", bound=Union[Russian, American, Chinese])


class Adapter:
    """Adapter implementation without inheritance. It can be used with any classes."""

    def __init__(self, nationality: Nationality, **adapted_methods: Callable):
        self.nationality = nationality
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """Redirects attribute calls to the nationality object instead of the adapter class"""
        return getattr(self.nationality, attr)

    def original_dict(self) -> dict:
        return self.nationality.__dict__
