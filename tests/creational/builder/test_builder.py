from patterns.creational.builder.builder import IphoneBuilder, RedmiBuilder, Director


def test_builder():
    director = Director()

    director.set_builder(IphoneBuilder())
    smartphone = director.build_smartphone()
    assert smartphone.company == "Apple Inc."
    assert smartphone.operating_system == "IOS"
    assert smartphone.logo == "Half-Bitten Apple"

    director.set_builder(RedmiBuilder())
    smartphone = director.build_smartphone()
    assert smartphone.company == "Xiaomi Inc."
    assert smartphone.operating_system == "Android"
    assert smartphone.logo == "MI"
