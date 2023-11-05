from patterns.behavioral.visitor.visitor import Theatre, Bank, Auditor, Director


def main():
    visitors = [Auditor(), Director()]

    theatre = Theatre()
    for visitor in visitors:
        theatre.accept(visitor)

    print("\n")

    bank = Bank()
    for visitor in visitors:
        bank.accept(visitor)


if __name__ == "__main__":
    main()
