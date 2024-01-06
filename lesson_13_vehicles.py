from abc import ABC, abstractmethod
from typing import Type

class Vehicle(ABC):
    def __init__(self, make: str, fuel_tank: int | float, remaining_fuel: int | float, speed: int, mileage: int):
        self.make = make
        self.fuel_tank = fuel_tank
        self.remaining_fuel = remaining_fuel
        self.speed = speed
        self.mileage = mileage
    @abstractmethod
    def __str__(self) -> str:
        return f"{self.make} ({self.__class__.__name__}): Fuel: {self.remaining_fuel}/{self.fuel_tank} liters, Speed: {self.speed} km/h, Mileage: {self.mileage} km"

    def tank(self, amount: float):
        self.remaining_fuel = min(self.fuel_tank, self.remaining_fuel + amount)

    def transfusion_fuel(self, another_vehicle: Type["Vehicle"], available_amount: float):
        free_space = another_vehicle.fuel_tank - another_vehicle.remaining_fuel
        available_amount = min(self.remaining_fuel, free_space)

        another_vehicle.remaining_fuel += available_amount
        self.remaining_fuel -= available_amount

class Car(Vehicle):
    def __init__(self, make: str, fuel_tank: int | float, remaining_fuel: int | float, speed: int, mileage: int, passagers: int, airbags: bool):
        super().__init__(make, fuel_tank, remaining_fuel, speed, mileage)
        self.passagers = passagers
        self.airbags = airbags


class Motorcycle(Vehicle):
    def __init__(self, make: str, fuel_tank: int | float, remaining_fuel: int | float, speed: int, mileage: int, cradle: bool):
        super().__init__(make, fuel_tank, remaining_fuel, speed, mileage)
        self.cradle = cradle
