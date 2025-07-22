from prac_09.car import Car

class UnreliableCar(Car):
    """Unreliable version of car."""
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

