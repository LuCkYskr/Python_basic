from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("В топливном баке нет топлива.")
        else:
            print("Двигатель находится в заведенном состоянии")

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            print(f"Пройденно {distance} km, осталось топлива: {self.fuel}")
        else:
            raise NotEnoughFuel(f"Для преодоления {distance} km. недостаточно топлива")


