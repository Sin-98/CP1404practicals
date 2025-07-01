"""
Guitar test
Estimate: 30 minutes
Actual:    minutes
"""

from prac_06.guitar import Guitar

def main():
    """Test Guitar class."""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1789.96)
    print(f"{guitar.name} get_age() - Expected {103}. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {12}. Got {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")

main()