from patterns.behavioral.iterator.iterator_via_generator import numbers_up_to
from patterns.behavioral.iterator.iterator_pythonic import MyCollection
from patterns.behavioral.iterator.iterator_classic import MyNumberCollection


def main():
    print("Iterator via generator: ")
    for i in numbers_up_to(2):
        print(i)

    print("\nPythonic iterator:")
    collection = MyCollection(["one", "two"])
    for item in collection:
        print(item)

    print("\nClassic iterator:")
    collection = MyNumberCollection(["one", "two"])
    iterator = collection.get_iterator()
    while iterator.has_next():
        print(iterator.next())


if __name__ == "__main__":
    main()
