import pytest
from patterns.creational.factory.main import get_developer_factory
from patterns.creational.factory.developer import Developer, JavaDeveloper, PythonDeveloper
from patterns.creational.factory.developer_factory import DeveloperFactory, JavaDeveloperFactory, PythonDeveloperFactory


def test_factory():
    java_developer_factory = get_developer_factory("Java")
    java_developer = java_developer_factory.create_developer()
    java_developer.write_code()
    assert isinstance(java_developer_factory, DeveloperFactory)
    assert isinstance(java_developer, Developer)
    assert isinstance(java_developer, JavaDeveloper)

    python_developer_factory = get_developer_factory("Python")
    python_developer = python_developer_factory.create_developer()
    python_developer.write_code()
    assert isinstance(python_developer, Developer)
    assert isinstance(python_developer_factory, DeveloperFactory)
    assert isinstance(python_developer, PythonDeveloper)
