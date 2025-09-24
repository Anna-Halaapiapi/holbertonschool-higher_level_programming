#!/usr/bin/env python3
"""
This module provides the abstract class Animal.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This abstract class defines an Animal.
    """

    @abstractmethod
    def sound(self):
        """
        This abstract method is intentionally empty.
        """
        pass


class Dog(Animal):
    """
    This class defines a dog and inherits from
    abstract class Animal.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    This class defines a cat and inherits from
    abstract class Animal.
    """
    def sound(self):
        return "Meow"
