from patterns.creational.prototype.prototype import Prototype, PrototypeContainer


def test_prototype():
    container = PrototypeContainer()
    value = 123
    list_of_objects = [777, [1, 2, 3], {"a": 1, "b": 2}]
    prototype = Prototype(value, list_of_objects, container)
    container.add_prototype(prototype)

    copied_prototype = prototype.copy()
    copied_prototype.list_of_objects.append("something")
    copied_prototype.list_of_objects[1][0] = 0
    copied_prototype.list_of_objects[2].update({"c": 3})
    assert copied_prototype.list_of_objects == prototype.list_of_objects
    assert copied_prototype.value == prototype.value
    assert copied_prototype.container == prototype.container
    assert id(copied_prototype.container.prototypes[0].container.prototypes[0]) == \
           id(copied_prototype.container.prototypes[0])
    assert id(copied_prototype.container.prototypes[0].container) == id(copied_prototype.container)

    deep_copied_prototype = prototype.deepcopy()
    deep_copied_prototype.list_of_objects.append("something2")
    deep_copied_prototype.list_of_objects[1][0] = 10
    deep_copied_prototype.list_of_objects[2].update({"d": 4})
    assert deep_copied_prototype.list_of_objects != prototype.list_of_objects
    assert deep_copied_prototype.value == prototype.value
    assert deep_copied_prototype.container != prototype.container
    assert id(deep_copied_prototype.container.prototypes[0].container.prototypes[0]) == \
           id(deep_copied_prototype.container.prototypes[0])
    assert id(deep_copied_prototype.container.prototypes[0].container) == id(deep_copied_prototype.container)
