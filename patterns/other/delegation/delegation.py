from typing import Any, Callable, Union


class Delegate:
    def __init__(self) -> None:
        self.field = 99

    def do_something(self):
        print("Doing something")


class Delegator:
    def __init__(self, delegate: Delegate) -> None:
        self.delegate = delegate

    def __getattr__(self, name: str) -> Union[Any, Callable]:
        attr = getattr(self.delegate, name)

        if not callable(attr):
            return attr

        def wrapper(*args, **kwargs):
            return attr(*args, **kwargs)

        return wrapper
