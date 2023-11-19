from prac_06.car import Car
from random import randint



class UnreliableCar(Car):
    """Class derived class for an UnreliableCar that inherits from Car."""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Generate a random number between 0 and 100, and only drive the car if that number is less than the car's
        reliability."""
        random_number = randint(1, 100)
        if random_number > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven




