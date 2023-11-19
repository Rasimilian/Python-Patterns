from typing import Union


class Car:
    def __str__(self):
        return "Car"


class Motorcycle:
    def __str__(self):
        return "Motorcycle"


class CoupledGarage:
    def __init__(self):
        self.vehicle = Car()

    def store(self):
        print(f"Storing {self.vehicle}")


class DecoupledGarage:
    """Class doesn't depend on a concrete vehicle and receives it from outside."""

    def __init__(self, vehicle: Union[Car, Motorcycle]):
        self.vehicle = vehicle

    def store(self):
        print(f"Storing {self.vehicle}")


class DecoupledGarage2:
    """Encapsulation violation due to the public setter method."""

    def set_vehicle(self, vehicle: Union[Car, Motorcycle]):
        self.vehicle = vehicle

    def store(self):
        print(f"Storing {self.vehicle}")
