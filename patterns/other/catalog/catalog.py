

class Catalog:
    def __init__(self, param: str):
        self.param = param
        self.func_dict = {"func1": self.func1, "func2": self.func2}

    def func1(self):
        print("Executing func1")

    def func2(self):
        print("Executing func2")

    def main_func(self):
        self.func_dict[self.param]()
