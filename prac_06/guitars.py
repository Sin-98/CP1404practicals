"""
Guitars
Estimate: 30 minutes
Actual:    minutes
"""

from prac_06.guitar import Guitar

def main():
    """Play guitar using Guitar class."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        name = input("Name: ")

