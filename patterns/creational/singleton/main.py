from typing import Union, Type
from threading import Thread

from patterns.creational.singleton import singleton_pythonic
from patterns.creational.singleton import singleton_metaclass
from patterns.creational.singleton import singleton_conventional


def get_singleton(singleton: Union[Type[singleton_metaclass.Singleton],
                                   Type[singleton_conventional.Singleton],
                                   Type[singleton_pythonic.Singleton]],
                  value: str) -> None:
    if singleton == singleton_conventional.Singleton:
        singleton_ = singleton.get_instance(value)
        print(singleton_.value)
        print("instance id:", id(singleton_))
    else:
        singleton_ = singleton(value)
        print(singleton_.value)
        print("instance id:", id(singleton_))


def main():
    # Metaclass implementation of Singleton
    process1 = Thread(target=get_singleton, args=(singleton_metaclass.Singleton, "instance1"))
    process2 = Thread(target=get_singleton, args=(singleton_metaclass.Singleton, "instance2"))
    process1.start()
    process2.start()

    # Pythonic implementation of Singleton
    process1 = Thread(target=get_singleton, args=(singleton_pythonic.Singleton, "instance1"))
    process2 = Thread(target=get_singleton, args=(singleton_pythonic.Singleton, "instance2"))
    process1.start()
    process2.start()

    # Conventional implementation of Singleton
    process1 = Thread(target=get_singleton, args=(singleton_conventional.Singleton, "instance1"))
    process2 = Thread(target=get_singleton, args=(singleton_conventional.Singleton, "instance2"))
    process1.start()
    process2.start()


if __name__ == "__main__":
    main()
