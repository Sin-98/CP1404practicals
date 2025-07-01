"""
Guitar
Estimate: 30 minutes
Actual:    minutes
"""
from datetime import date

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