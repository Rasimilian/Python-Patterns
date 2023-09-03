from patterns.creational.lazy_evaluation.lazy_evaluation import President


def main():
    mr_president = President("Chinese", "Beijing")
    print(mr_president.__dict__)

    mr_president.greeting()
    print(mr_president.__dict__)
    mr_president.greeting()
    print(mr_president.__dict__)

    mr_president.colleagues
    print(mr_president.__dict__)
    mr_president.colleagues
    print(mr_president.__dict__)

    mr_president.friends
    print(mr_president.__dict__)
    mr_president.friends
    print(mr_president.__dict__)

    mr_president.siblings
    print(mr_president.__dict__)
    mr_president.siblings
    print(mr_president.__dict__)


if __name__ == "__main__":
    main()
