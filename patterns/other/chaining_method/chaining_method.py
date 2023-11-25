

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, val: float):
        self.result += val
        return self

    def multiply(self, val: float):
        self.result *= val
        return self

    def get_result(self):
        return self.result
