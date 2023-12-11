from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi that inherits from Taxi"""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise an SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def get_fancy_fare(self):
        """Get the charge which equals flagfall + fare"""
        return self.flagfall + super().get_fare()
