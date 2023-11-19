from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    """Write a taxi simulator program that uses your Taxi and SilverServiceTaxi classes."""
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxi available")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            # Once taxi chosen it can proceed to drive and add to total bill
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                taxi_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${taxi_cost:.2f}")
                total_bill += taxi_cost
            else:
                # No taxi chosen to drive
                print("You need to choose a taxi before you can drive")
        print(f"Invalid option \nBill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxis with corresponding number to be selected in choice c."""
    for i, taxi in enumerate(taxis):
        print(f"{i: 3} - {taxi}")


main()
