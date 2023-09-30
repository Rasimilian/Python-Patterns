from patterns.structural.flyweight.flyweight import SmartphoneMarket
from patterns.structural.flyweight.flyweight_pythonic import Smartphone


def main():
    market = SmartphoneMarket([
        ("iPhone", "15", "Grey"),
        ("Xiaomi", "9T", "Black")
    ])
    print(f"Number of stored smartphones: {market.list_cached_smartphones()}")
    print("\t")

    phone_1 = market.get_smartphone(("Xiaomi", "9T", "White"))
    phone_1.make_call()
    print("\t")
    phone_2 = market.get_smartphone(("iPhone", "14", "White"))
    phone_2.make_call()
    print("\t")

    print(f"Number of stored smartphones: {market.list_cached_smartphones()}")
    print('\t')

    print("Pythonic implementation:")
    phone_1 = Smartphone(manufacturer="iPhone", model="15", color="Grey")
    phone_1.make_call()
    print('\t')

    phone_2 = Smartphone(manufacturer="iPhone", model="15", color="Black")
    phone_2.make_call()
    print(f"phone_1 == phone_2: {phone_1 == phone_2}")
    print(f"phone_1 is phone_2: {phone_1 is phone_2}")
    print(f"Number of stored smartphones: {Smartphone.list_cached_smartphones()}")
    print('\t')

    phone_3 = Smartphone(manufacturer="Xiaomi", model="9T", color="White")
    phone_3.make_call()
    print(f"Number of stored smartphones: {Smartphone.list_cached_smartphones()}")
    print("\t")

    phone_3.memory = "128 Gb"
    phone_4 = Smartphone(manufacturer="Xiaomi", model="9T", color="Blue")
    phone_4.make_call()
    print(f"phone_3 == phone_4: {phone_3 == phone_4}")
    print(f"phone_3 is phone_4: {phone_3 is phone_4}")
    print(hasattr(phone_4, 'memory'))
    print("\t")

    Smartphone._pool.clear()
    print(f"Number of stored smartphones: {Smartphone.list_cached_smartphones()}")
    phone_5 = Smartphone(manufacturer="Xiaomi", model="9T", color="Green")
    phone_5.make_call()
    print(f"phone_3 == phone_5: {phone_3 == phone_5}")
    print(f"phone_3 is phone_5: {phone_3 is phone_5}")
    print(hasattr(phone_5, 'memory'))
    print(f"Number of stored smartphones: {Smartphone.list_cached_smartphones()}")


if __name__ == "__main__":
    main()
