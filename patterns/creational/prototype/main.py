from patterns.creational.prototype.prototype import Prototype, PrototypeContainer


def main():
    container = PrototypeContainer()
    value = 123
    list_of_objects = [777, [1, 2, 3], {"a": 1, "b": 2}]
    prototype = Prototype(value, list_of_objects, container)
    container.add_prototype(prototype)

    print("Copy")
    copied_prototype = prototype.copy()

    copied_prototype.list_of_objects.append("something")
    print(copied_prototype.list_of_objects, prototype.list_of_objects)

    copied_prototype.list_of_objects[1][0] = 0
    print(copied_prototype.list_of_objects[1], prototype.list_of_objects[1])

    copied_prototype.list_of_objects[2].update({"c": 3})
    print(copied_prototype.list_of_objects[2], prototype.list_of_objects[2])

    print("Recursive Prototype's ID: ",
          id(copied_prototype.container.prototypes[0].container.prototypes[0]),
          id(copied_prototype.container.prototypes[0]))

    print("Recursive Container's ID: ",
          id(copied_prototype.container.prototypes[0].container),
          id(copied_prototype.container))

    print("\nDeep copy")
    deep_copied_prototype = prototype.deepcopy()

    deep_copied_prototype.list_of_objects.append("something2")
    print(deep_copied_prototype.list_of_objects, prototype.list_of_objects)

    deep_copied_prototype.list_of_objects[1][0] = 10
    print(deep_copied_prototype.list_of_objects[1], prototype.list_of_objects[1])

    deep_copied_prototype.list_of_objects[2].update({"d": 4})
    print(deep_copied_prototype.list_of_objects[2], prototype.list_of_objects[2])

    print("Recursive Prototype's ID: ",
          id(deep_copied_prototype.container.prototypes[0].container.prototypes[0]),
          id(deep_copied_prototype.container.prototypes[0]))

    print("Recursive Container's ID: ",
          id(deep_copied_prototype.container.prototypes[0].container),
          id(deep_copied_prototype.container))


if __name__ == "__main__":
    main()
