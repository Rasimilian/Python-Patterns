from __future__ import annotations

from typing import Dict, Type


class RegistryBase(type):
    REGISTRY: Dict[str, Type[BaseRegisteredClass]] = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls


class BaseRegisteredClass(metaclass=RegistryBase):
    pass


class ExtendedRegisteredClass(BaseRegisteredClass):
    pass
