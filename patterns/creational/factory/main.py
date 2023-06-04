from patterns.creational.factory.developer_factory import DeveloperFactory, JavaDeveloperFactory, PythonDeveloperFactory


def get_developer_factory(language: str) -> DeveloperFactory:
    languages = {"Java": JavaDeveloperFactory,
                 "Python": PythonDeveloperFactory}
    return languages[language]()


if __name__ == "__main__":
    java_developer_factory = get_developer_factory("Java")
    java_developer = java_developer_factory.create_developer()
    java_developer.write_code()

    python_developer_factory = get_developer_factory("Python")
    python_developer = python_developer_factory.create_developer()
    python_developer.write_code()


