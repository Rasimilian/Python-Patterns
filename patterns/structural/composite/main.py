from patterns.structural.composite.composite import Electron, Compound


def main():
    electron = Electron(1)
    electron2 = Electron(2)
    electron3 = Electron(3)

    print("First compound:")
    compound = Compound(1)
    compound.add(electron)
    compound.add(electron2)
    compound.rotate()

    print("\nSecond compound:")
    compound2 = Compound(2)
    compound2.add(electron3)
    compound2.add(compound)
    compound2.rotate()

    print("\nSecond compound again:")
    compound2.remove(compound)
    compound2.rotate()


if __name__ == "__main__":
    main()
