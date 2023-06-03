from patterns.creational.factory.base import *


class Developer(ABC):
    @abstractmethod
    def write_code(self):
        pass


class JavaDeveloper(Developer):
    def write_code(self):
        print("Java developer writes a Java code.")


class PythonDeveloper(Developer):
    def write_code(self):
        print("Python developer writes a Python code.")
