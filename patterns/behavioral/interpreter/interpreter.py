from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self, text: str) -> bool:
        pass


class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, text: str) -> bool:
        return self.expr1.interpret(text) and self.expr2.interpret(text)


class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, text: str) -> bool:
        return self.expr1.interpret(text) or self.expr2.interpret(text)


class TerminalExpression(Expression):
    def __init__(self, data: str):
        self.data = data

    def interpret(self, text: str) -> bool:
        return text in self.data
