#!/usr/bin/env python3
"""
This module provides the abstract class Shape.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    defines a shape.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    defines circle. inherits from abstract class Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            raise ValueError("radius cannot be less than 0")
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        if self.radius < 0:
            raise ValueError("radius cannot be less than 0")
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    defines rectangle. inherits from abstract class Shape.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)


def shape_info(obj):
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
