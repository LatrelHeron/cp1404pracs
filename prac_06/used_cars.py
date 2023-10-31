"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "Car")
    my_car.drive(30)
    print(f"{my_car.vehicle} has fuel: {my_car.fuel}")
    print(my_car)

    new_car = Car(100, "Limo")
    new_car.add_fuel(20)
    print(f"{new_car.vehicle} has fuel: {new_car.fuel}")
    driven = 115
    new_car.drive(driven)
    print(f"{new_car.vehicle} after having {driven} now has fuel: {new_car.fuel}")


main()
