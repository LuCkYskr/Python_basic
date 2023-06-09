"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, engine=0) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine):
        self.engine = engine
