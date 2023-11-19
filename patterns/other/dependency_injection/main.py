from patterns.other.dependency_injection.dependency_injection import Car, \
    Motorcycle, CoupledGarage, DecoupledGarage, DecoupledGarage2


def main():
    car = Car()
    motorcycle = Motorcycle()

    print("Coupled Garage:")
    coupled_garage = CoupledGarage()
    coupled_garage.store()

    print("\nDecoupled Garage:")
    decoupled_garage = DecoupledGarage(car)
    decoupled_garage.store()
    decoupled_garage = DecoupledGarage(motorcycle)
    decoupled_garage.store()

    print("\nDecoupled Garage2:")
    decoupled_garage2 = DecoupledGarage2()
    decoupled_garage2.set_vehicle(car)
    decoupled_garage2.store()
    decoupled_garage2 = DecoupledGarage2()
    decoupled_garage2.set_vehicle(motorcycle)
    decoupled_garage2.store()


if __name__ == "__main__":
    main()
