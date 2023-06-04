from patterns.creational.factory.developer_factory import get_developer_factory


def main():
    """
    A factory method creates two developers writing in Java and Python.
    """
    java_developer_factory = get_developer_factory("Java")
    java_developer = java_developer_factory.create_developer()
    java_developer.write_code()

    python_developer_factory = get_developer_factory("Python")
    python_developer = python_developer_factory.create_developer()
    python_developer.write_code()


if __name__ == "__main__":
    main()
