import pytest

from patterns.creational.singleton import singleton_conventional
from patterns.creational.singleton import singleton_pythonic
from patterns.creational.singleton import singleton_metaclass


def test_singleton():
    # Metaclass implementation of Singleton
    singleton1 = singleton_metaclass.Singleton("instance1")
    singleton2 = singleton_metaclass.Singleton("instance2")
    assert id(singleton1) == id(singleton2)
    assert singleton1.value == singleton2.value
    assert singleton1 is singleton2

    # Pythonic implementation of Singleton
    singleton1 = singleton_pythonic.Singleton("instance1")
    singleton2 = singleton_pythonic.Singleton("instance2")
    assert id(singleton1) == id(singleton2)
    assert singleton1.value == singleton2.value
    assert singleton1 is singleton2

    # Conventional implementation of Singleton
    singleton1 = singleton_conventional.Singleton.get_instance("instance1")
    singleton2 = singleton_conventional.Singleton.get_instance("instance2")
    assert id(singleton1) == id(singleton2)
    assert singleton1.value == singleton2.value
    assert singleton1 is singleton2
