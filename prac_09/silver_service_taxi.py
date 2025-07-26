from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A silver service taxi is a fancy version of taxi with higher fares and a flag fall."""

    flagfall = 4.50

    def __init__(self, name,fuel, fanciness):
        """initialise a silver service taxi with a fanciness multiplier."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare for the taxi trip including the flagfall. """
        return super().get_fare()+ self.flagfall

    def __str__(self):
        """Return a string representation of the taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

