"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car("Limo", 100) # create a new car object called "limo" that is initialised with 100 fuel.
    limo.add_fuel(20) #Add 20 more units of fuel.
    print (f"Limo has fuel:{limo.fuel}") # print the amount of fuel in the car.

    distance_driven = limo.drive(115) #attempt to drive the car 115km
    print (f"limo has driven {distance_driven} km. ")

    print(limo) # print the car object (uses__str__ method).
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)


main()