import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Read, display, add and save guitars."""
    guitars = load_guitars(FILENAME)
    print("My guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    new_guitars = get_new_guitars()
    guitars += new_guitars

    save_guitars(FILENAME, guitars)

def load_guitars(guitars):
    """Read guitars from a file and return a list of Guitar objects."""
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """Display a list of Guitar objects."""
    for guitar in guitars:
        print(guitar)

def get_new_guitars():
    """Get the user to add new guitars and return them as a list."""
    new_guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        new_guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("Name: ")
    return new_guitars

def save_guitars(FILENAME, guitars):
    """Write guitars to a file."""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

main()