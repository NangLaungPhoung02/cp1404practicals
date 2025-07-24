"""
CP1404
unreliable_car.py
estimate time : 30 minutes
Actual  total two file time : 45 minutes

"""
from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """A car that might not drive depending on its reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on reliability."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0