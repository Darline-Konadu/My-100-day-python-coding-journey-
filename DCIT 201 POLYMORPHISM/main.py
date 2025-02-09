from abc import ABC, abstractmethod


# Abstract Class Vehicle
class Vehicle(ABC):
    def __init__(self, vehicle_id: str, model: str, fuel_level: float):
        self.vehicle_id = vehicle_id
        self.model = model
        self.fuel_level = fuel_level

    def refuel(self, liters: float):
        self.fuel_level += liters
        print(f"{self.model} refueled. New fuel level: {self.fuel_level} liters.")

    @abstractmethod
    def calculate_range(self):
        pass


# Derived Class Car
class Car(Vehicle):
    def __init__(self, vehicle_id: str, model: str, fuel_level: float, fuel_efficiency: float):
        super().__init__(vehicle_id, model, fuel_level)
        self.fuel_efficiency = fuel_efficiency

    def calculate_range(self):
        range_km = self.fuel_level * self.fuel_efficiency
        print(f"Car {self.model} can travel {range_km} km with current fuel level.")


# Independent Class TransportationManager
class TransportationManager:
    @staticmethod
    def operate_vehicle(vehicle: Vehicle):
        vehicle.calculate_range()


# Implementation
car1 = Car("O243691528", "Sedan", 50, 15)

# Refuel Car
car1.refuel(10)

# Operate Vehicle
manager = TransportationManager()
manager.operate_vehicle(car1)
