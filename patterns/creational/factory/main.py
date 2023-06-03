from developer_factory import JavaDeveloperFactory, PythonDeveloperFactory


if __name__ == "__main__":
    java_developer_factory = JavaDeveloperFactory()
    java_developer = java_developer_factory.create_developer()
    java_developer.write_code()

    python_developer_factory = PythonDeveloperFactory()
    python_developer = python_developer_factory.create_developer()
    python_developer.write_code()


