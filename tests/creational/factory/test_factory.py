import pytest

from patterns.creational.factory.developer_factory import *


@pytest.mark.parametrize("language, expected_factory, expected_developer",
[
    ("Java", JavaDeveloperFactory, JavaDeveloper),
    ("Python", PythonDeveloperFactory, PythonDeveloper)
])
def test_factory(language: str,
                 expected_factory: Type[DeveloperFactory_],
                 expected_developer: Type[Developer_]):
    developer_factory = get_developer_factory(language)
    developer = developer_factory.create_developer()
    developer.write_code()
    assert isinstance(developer_factory, DeveloperFactory)
    assert isinstance(developer_factory, expected_factory)
    assert isinstance(developer, Developer)
    assert isinstance(developer, expected_developer)
