from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi"""
    taxi = SilverServiceTaxi("Hummer", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fancy_fare())


main()
