from patterns.creational.borg.borg import SubBorg, AnotherBorg


def main():
    borg1 = SubBorg()
    borg2 = SubBorg()
    print(borg1.state, borg2.state)

    borg1.state = "Borg1"
    borg2.state = "Borg2"
    borg3 = SubBorg()
    print(borg1.state, borg2.state, borg3.state)

    borg4 = SubBorg("Borg4")
    print(borg1.state, borg2.state, borg3.state, borg4.state)

    # Borg with another _shared_state not shared with 1-4 Borgs
    borg5 = AnotherBorg("Borg5")
    print(borg1.state, borg2.state, borg3.state, borg4.state, borg5.state)


if __name__ == "__main__":
    main()
