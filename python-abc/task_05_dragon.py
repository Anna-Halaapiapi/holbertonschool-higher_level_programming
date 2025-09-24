#!/usr/bin/env python3
"""
This module provides the SwimMixin, FlyMixin, Dragon classes.
"""


class SwimMixin:
    """
    defines SwimMixin
    """
    
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    defines FlyMixin
    """

    def fly(self):
        print("The creature flies!")
    

class Dragon(SwimMixin, FlyMixin):
    """
    defines Dragon
    """

    def roar(self):
        print("The dragon roars!")

    def appearance(self):
        print("The dragon has purple scales and yellow horns.")
      
    def abilities(self):
        print("The dragon breathes fire!")

    def name(self):
        print("The dragon's name is Spyro.")
