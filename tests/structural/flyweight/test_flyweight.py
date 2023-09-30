from patterns.structural.flyweight.flyweight import SmartphoneMarket
from patterns.structural.flyweight.flyweight_pythonic import Smartphone
from patterns.structural.flyweight.flyweight_metaclass import SmartphoneM


def test_flyweight(capsys):
    market = SmartphoneMarket([
        ("iPhone", "15", "Grey"),
        ("Xiaomi", "9T", "Black")
    ])
    assert market.list_cached_smartphones() == 2

    phone_1 = market.get_smartphone(("Xiaomi", "9T", "White"))
    phone_1.make_call()
    out, err = capsys.readouterr()
    assert out == "Reused cached smartphone: Xiaomi_9T\nMaking call from the smartphone Xiaomi 9T\n"

    phone_2 = market.get_smartphone(("Xiaomi", "9T", "Black"))
    phone_2.make_call()
    out, err = capsys.readouterr()
    assert out == "Reused cached smartphone: Xiaomi_9T\nMaking call from the smartphone Xiaomi 9T\n"
    assert phone_1 == phone_2
    assert phone_1 is phone_2

    phone_3 = market.get_smartphone(("iPhone", "14", "White"))
    phone_3.make_call()
    out, err = capsys.readouterr()
    assert out == "Added new smartphone to the cache: iPhone_14\nMaking call from the smartphone iPhone 14\n"

    assert market.list_cached_smartphones() == 3


def test_flyweight_pythonic(capsys):
    phone_1 = Smartphone(manufacturer="iPhone", model="15", color="Grey")
    phone_1.make_call()
    out, err = capsys.readouterr()
    assert out == "Added new smartphone to the cache: iPhone_15\nMaking call from the smartphone iPhone 15\n"

    phone_2 = Smartphone(manufacturer="iPhone", model="15", color="Black")
    phone_2.make_call()
    out, err = capsys.readouterr()
    assert out == "Reused cached smartphone: iPhone_15\nMaking call from the smartphone iPhone 15\n"
    assert phone_1 == phone_2
    assert phone_1 is phone_2
    assert Smartphone.list_cached_smartphones() == 1

    phone_3 = Smartphone(manufacturer="Xiaomi", model="9T", color="White")
    phone_3.make_call()
    out, err = capsys.readouterr()
    assert out == "Added new smartphone to the cache: Xiaomi_9T\nMaking call from the smartphone Xiaomi 9T\n"
    assert Smartphone.list_cached_smartphones() == 2

    phone_3.memory = "128 Gb"
    phone_4 = Smartphone(manufacturer="Xiaomi", model="9T", color="Blue")
    phone_4.make_call()
    out, err = capsys.readouterr()
    assert out == "Reused cached smartphone: Xiaomi_9T\nMaking call from the smartphone Xiaomi 9T\n"
    assert phone_3 == phone_4
    assert phone_3 is phone_4
    assert Smartphone.list_cached_smartphones() == 2
    assert hasattr(phone_4, 'memory')

    Smartphone._pool.clear()
    assert Smartphone.list_cached_smartphones() == 0
    phone_5 = Smartphone(manufacturer="Xiaomi", model="9T", color="Green")
    phone_5.make_call()
    out, err = capsys.readouterr()
    assert out == "Added new smartphone to the cache: Xiaomi_9T\nMaking call from the smartphone Xiaomi 9T\n"
    assert phone_3 != phone_5
    assert phone_3 is not phone_5
    assert Smartphone.list_cached_smartphones() == 1
    assert not hasattr(phone_5, 'memory')


def test_flyweight_metaclass(capsys):
    phone_1 = SmartphoneM(manufacturer="Xiaomi", model="9T", color="Blue")
    phone_1.make_call()
    out, err = capsys.readouterr()
    assert out == "Added new smartphone to the cache: Xiaomi_9T\nMaking call from the smartphone Xiaomi 9T\n"

    phone_2 = SmartphoneM(manufacturer="Xiaomi", model="9T", color="White")
    phone_2.make_call()
    out, err = capsys.readouterr()
    assert out == "Reused cached smartphone: Xiaomi_9T\nMaking call from the smartphone Xiaomi 9T\n"
    assert phone_1 == phone_2
    assert phone_1 is phone_2
    assert SmartphoneM.list_cached_smartphones() == 1

    phone_3 = SmartphoneM(manufacturer="iPhone", model="15", color="Grey")
    phone_3.make_call()
    out, err = capsys.readouterr()
    assert out == "Added new smartphone to the cache: iPhone_15\nMaking call from the smartphone iPhone 15\n"
    assert SmartphoneM.list_cached_smartphones() == 2
