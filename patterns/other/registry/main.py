from patterns.other.registry.registry import RegistryBase, BaseRegisteredClass


def main():
    print(list(RegistryBase.REGISTRY))

    class AnotherExtendedRegisteredClass(BaseRegisteredClass):
        pass

    print(list(RegistryBase.REGISTRY))


if __name__ == "__main__":
    main()
