from patterns.creational.builder.builder import IphoneBuilder, RedmiBuilder, Director


def main():
    director = Director()

    director.set_builder(IphoneBuilder())
    smartphone = director.build_smartphone()
    print(smartphone)

    director.set_builder(RedmiBuilder())
    smartphone = director.build_smartphone()
    print(smartphone)


if __name__ == "__main__":
    main()
