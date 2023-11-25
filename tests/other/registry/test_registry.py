from patterns.other.registry.registry import RegistryBase, BaseRegisteredClass


def test_registry():
    assert list(RegistryBase.REGISTRY) == ['BaseRegisteredClass', 'ExtendedRegisteredClass']

    class AnotherExtendedRegisteredClass(BaseRegisteredClass):
        pass

    assert list(RegistryBase.REGISTRY) == ['BaseRegisteredClass', 'ExtendedRegisteredClass', 'AnotherExtendedRegisteredClass']
