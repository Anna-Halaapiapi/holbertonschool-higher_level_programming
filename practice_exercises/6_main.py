#!/usr/bin/python3

Car = __import__('6_vehicleclass_inheritance').Car
Truck = __import__('6_vehicleclass_inheritance').Truck


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
