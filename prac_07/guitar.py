from datetime import date
VINTAGE_AGE = 50

class Guitar:
    """Represents details of a guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the Guitar."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if the Guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year