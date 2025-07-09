"""
Project
Estimate: 60 minutes
Actual:    minutes
"""
import datetime


class Project:
    """A class to represent a project."""
    def __init__(self, name, start_date, priority: int, cost_estimate: float, completion_percentage: int):
        """Initialize a project."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Display output."""
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Less than."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if the project is complete."""
        return self.completion_percentage >= 100