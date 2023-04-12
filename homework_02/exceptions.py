"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """В топливном баке нет топлива."""
    pass


class NotEnoughFuel(Exception):
    """Топлива в топливном бане недостаточнодля
    преодоления заданного расстояния."""
    pass


class CargoOverload(Exception):
    """Транспортное средство перегружено."""
    pass
