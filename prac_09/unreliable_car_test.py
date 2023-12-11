from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar"""
    reliable_car = UnreliableCar("Good Car", 100, 200)
    unreliable_car = UnreliableCar("Bad Car", 100, -100)
    random_reliable_car = UnreliableCar("Random Car", 100, 50)

    #Taken from solution
    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{reliable_car.name:12} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name:12} drove {unreliable_car.drive(i):2}km")
        print(f"{random_reliable_car.name:12} drove {random_reliable_car.drive(i):2}km")

    print(reliable_car)
    print(unreliable_car)
    print(random_reliable_car)


main()
