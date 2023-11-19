from patterns.other.dependency_injection.dependency_injection import Car, \
    Motorcycle, CoupledGarage, DecoupledGarage, DecoupledGarage2


def test_dependency_injection(capsys):
    car = Car()
    motorcycle = Motorcycle()

    coupled_garage = CoupledGarage()
    coupled_garage.store()
    out, err = capsys.readouterr()
    assert out == "Storing Car\n"
    assert coupled_garage.vehicle != car

    decoupled_garage = DecoupledGarage(car)
    decoupled_garage.store()
    out, err = capsys.readouterr()
    assert out == "Storing Car\n"
    assert decoupled_garage.vehicle == car

    decoupled_garage = DecoupledGarage(motorcycle)
    decoupled_garage.store()
    out, err = capsys.readouterr()
    assert out == "Storing Motorcycle\n"
    assert decoupled_garage.vehicle == motorcycle

    decoupled_garage2 = DecoupledGarage2()
    decoupled_garage2.set_vehicle(car)
    decoupled_garage2.store()
    out, err = capsys.readouterr()
    assert out == "Storing Car\n"
    assert decoupled_garage2.vehicle == car

    decoupled_garage2 = DecoupledGarage2()
    decoupled_garage2.set_vehicle(motorcycle)
    decoupled_garage2.store()
    out, err = capsys.readouterr()
    assert out == "Storing Motorcycle\n"
    assert decoupled_garage2.vehicle == motorcycle
