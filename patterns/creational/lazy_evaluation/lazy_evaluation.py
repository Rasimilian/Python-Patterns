from functools import update_wrapper, cached_property


def lazy_eval_func(func: callable):
    """A lazy evaluation decorator. When called for the first time,
    the wrapped function executes the code completely. Each next call, the already obtained result is just
    accessed without recalculation."""
    _name = "_cached_" + func.__name__

    def _lazy_eval(self):
        if not hasattr(self, _name):
            setattr(self, _name, func(self))
        return getattr(self, _name)

    return _lazy_eval


def lazy_eval_property(func: callable):
    """A lazy evaluation decorator. When called for the first time,
    the wrapped function executes the code completely. Each next call, the already obtained result is just
    accessed without recalculation."""
    _name = "_cached_" + func.__name__

    @property
    def _lazy_eval(self):
        if not hasattr(self, _name):
            setattr(self, _name, func(self))
        return getattr(self, _name)

    return _lazy_eval


class LazyProperty:
    def __init__(self, function: callable):
        self.function = function
        update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


class President:
    def __init__(self, nationality: str, location: str):
        self.nationality = nationality
        self.location = location
        self.greetings_num = 0
        self.colleagues_num = 0
        self.friends_num = 0
        self.siblings_num = 0

    @lazy_eval_func
    def greeting(self) -> str:
        # Time-consuming something
        self.greetings_num += 1
        something = "Ni Hao!"
        return something

    @lazy_eval_property
    def colleagues(self) -> str:
        # Time-consuming something
        self.colleagues_num += 1
        something = "Lots of colleagues"
        return something

    @LazyProperty
    def friends(self) -> str:
        # Time-consuming something
        self.friends_num += 1
        something = "Lots of friends"
        return something

    @cached_property
    def siblings(self) -> str:
        # Time-consuming something
        self.siblings_num += 1
        something = "Lots of siblings"
        return something
