"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        if self.cargo + value > self.max_cargo:
            raise CargoOverload("Транспортное средство перегружено.")
        else:
            self.cargo += value

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo


