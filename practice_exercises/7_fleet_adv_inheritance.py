#!/usr/bin/python3

#!/usr/bin/python3
"""
This module provides the Vehicle class.
"""


class Vehicle:
    """
    This Parent class defines a Vehicle.
    """
    def __init__(self, brand, year, maintenance_records=None):
        self.brand = brand
        self.year = year
        if maintenance_records == None:
            maintenance_records = []
        self.maintenance_records = maintenance_records

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
    
    # main. recds - getter
    @property
    def maintenance_records(self):
        return self.__maintenance_records

    # main. recds - setter
    @maintenance_records.setter
    def maintenance_records(self, value):
        """
        value is a list of dictionaries containing maintenance records
        """
        if not isinstance(value, list):
            raise TypeError("value must be a list")

        # loop through each dictionary in value list
        for item in value:
            if not isinstance(item, dict):
                raise TypeError("item in list must be a dictionary")

            if 'date' not in item:
                raise ValueError("date key doesn't exist")
            if 'description' not in item:
                raise ValueError("description key doesn't exist")
            if 'cost' not in item:
                raise ValueError("cost key doesn't exist")

            if len(item['date']) != 8:
                raise ValueError("date must be in format: DDMMYYYY")
            
            if not isinstance (item['date'], str):
                raise TypeError("date must be a string")           
            if not isinstance (item['description'], str):
                raise TypeError("description must be a string")
            if not isinstance (item['cost'], (float, int)):
                raise TypeError("cost must be a float or integer")

        self.__maintenance_records = value

    def add_maintenance_record(self, date, description, cost):
        """
        adds a single maintenance record
        """
        # create new dict with maintenance record
        new_dict = {"date": date, "description": description, "cost": cost}
        # get a copy of existing list to avoid modding original if validations fail
        existing_list = self.maintenance_records.copy()

        # append new entry to end of existing list
        existing_list.append(new_dict)

        # pass updated list back to setter
        self.maintenance_records = existing_list

    def describe(self):
        return(f"The brand is: {self.brand}, The year is: {self.year}")

class Car(Vehicle):
    """
    This child class inherits from the Vehicle class, and defines a Car.
    """
    def __init__(self, brand, year, doors, maintenance_records=None):
        super().__init__(brand, year, maintenance_records)
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
    def __init__(self, brand, year, payload_capacity, maintenance_records=None):
        super().__init__(brand, year, maintenance_records)
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

# Create a vehicle
v1 = Vehicle("Nissan", 2020)

# Print initial maintenance records (should be empty)
print("Initial records:", v1.maintenance_records)

# Add a valid maintenance record
v1.add_maintenance_record("15092025", "Oil change", 79.99)
v1.add_maintenance_record("20092025", "Tire rotation", 45.0)

# Print records after adding
print("\nAfter adding records:")
for record in v1.maintenance_records:
    print(record)

# Try to add an invalid record (wrong date format)
try:
    v1.add_maintenance_record("15-09-2025", "Invalid date format", 50)
except Exception as e:
    print("\nCaught expected error:", e)

# Try to assign an invalid list directly (e.g., contains non-dictionary)
try:
    v1.maintenance_records = ["not a dictionary"]
except Exception as e:
    print("\nCaught expected setter error:", e)

# Final state
print("\nFinal maintenance records:")
for record in v1.maintenance_records:
    print(record)
