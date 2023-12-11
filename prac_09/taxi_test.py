from taxi import Taxi

def main():
    """Test taxi"""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    drive = 40
    my_taxi.drive(drive)
    print(my_taxi)
    my_taxi.start_fare()
    new_fare_drive = 100
    my_taxi.drive(new_fare_drive)
    print(my_taxi)

main()


