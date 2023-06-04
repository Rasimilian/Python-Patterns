from . import *
from patterns.creational.factory.developer import Developer, JavaDeveloper, PythonDeveloper


class DeveloperFactory(ABC):
    @abstractmethod
    def create_developer(self) -> Developer:
        pass


class JavaDeveloperFactory(DeveloperFactory):
    def create_developer(self) -> JavaDeveloper:
        return JavaDeveloper()


class PythonDeveloperFactory(DeveloperFactory):
    def create_developer(self) -> PythonDeveloper:
        return PythonDeveloper()


def get_developer_factory(language: str) -> DeveloperFactory:
    languages = {"Java": JavaDeveloperFactory,
                 "Python": PythonDeveloperFactory}
    if language not in languages:
        raise ValueError("Unknown programming language!")

    return languages[language]()
