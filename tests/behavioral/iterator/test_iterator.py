from patterns.behavioral.iterator.iterator_via_generator import numbers_up_to
from patterns.behavioral.iterator.iterator_pythonic import MyCollection
from patterns.behavioral.iterator.iterator_classic import MyNumberCollection


def test_iterator():
    expected_numbers = ["one", "two"]

    for idx, item in enumerate(numbers_up_to(2)):
        assert item == expected_numbers[idx]

    collection = MyCollection(["one", "two"])
    for idx, item in enumerate(collection):
        assert item == expected_numbers[idx]

    collection = MyNumberCollection(["one", "two"])
    iterator = collection.get_iterator()
    idx = 0
    while iterator.has_next():
        assert iterator.next() == expected_numbers[idx]
        idx += 1
