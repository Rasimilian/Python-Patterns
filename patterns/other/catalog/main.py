from patterns.other.catalog.catalog import Catalog


def main():
    catalog1 = Catalog("func1")
    catalog1.main_func()

    catalog2 = Catalog("func2")
    catalog2.main_func()


if __name__ == "__main__":
    main()
