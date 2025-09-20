#!/usr/bin/python3
"""
This module provides the Vehicle class.
"""


class Vehicle:
    """
    This Parent class defines a Vehicle.
    """
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    # brand - getter
    @property
    def brand(self):
        return self.__brand
    
    # brand - setter
    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError("brand must be a string")
        self.__brand = value

    # year - getter
    @property
    def year(self):
        return self.__year

    # year - setter
    @year.setter
    def year(self, value):
        if not isinstance (value, int):
            raise TypeError("Year must be an integer")
        if len(str(value)) != 4:
            raise TypeError("Year must be in format: YYYY")
        self.__year = value
    
    def describe(self):
        return(f"The brand is: {self.brand}, The year is: {self.year}")
    
class Car(Vehicle):
    """
    This child class inherits from the Vehicle class, and defines a Car.
    """
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    # doors - getter
    @property
    def doors(self):
        return self.__doors

    # doors - setter
    @doors.setter
    def doors(self, value):
        if not isinstance(value, int):
            raise TypeError("doors must be an integer")
        if value < 0 or value > 10:
            raise ValueError("doors must be a value between 0 and 10")
        self.__doors = value
    
    def honk(self):
        print("Beep Beep!")

class Truck(Vehicle):
    """
    child class Truck that inherits from Vehicle class.
    """
    def __init__(self, brand, year, payload_capacity):
        super().__init__(brand, year)
        self.payload_capacity = payload_capacity

    # payload - getter
    @property
    def payload_capacity(self):
        return self.__payload_capacity

    # payload - setter
    @payload_capacity.setter
    def payload_capacity(self, value):
        if value <= 0:
            raise ValueError("value must not be less than or equal to 0")
        if not isinstance (value, int):
            raise TypeError("value must be an intger (kgs)")
        self.__payload_capacity = value
    
    def load_cargo(self):
        print(f"{super().describe()}, Payload Capacity: {self.payload_capacity}\nLoading up to {self.payload_capacity}kg of cargo.")


# Car = __import__('6_vehicleclass_inheritance').Car
# Truck = __import__('6_vehicleclass_inheritance').Truck


vehicles = [
    Car("Toyota", 2022, 4),
    Truck("Volvo", 2019, 2000),
    Car("Mazda", 2023, 2)
]

for item in vehicles:
    if isinstance(item, Car):
        print(item.describe())
        item.honk()
    if isinstance(item, Truck):
        item.load_cargo()
