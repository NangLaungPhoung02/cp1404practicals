class Car:
    """Represent a car object."""
    def __init__(self, name,fuel):
        self.name = name
        self.fuel = fuel
        self.odometer =0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer = {self.odometer}"

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        """Drive the car, using fuel. Return distance actually driven."""
        if self.distance > self.fuel:
            distance = self.fuel
        self.fuel -=distance
        self.odometer += distance
        return distance