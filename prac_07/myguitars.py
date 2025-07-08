from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Read, display, add and save guitars."""
    guitars = load_guitars(FILENAME)
    print("My guitars:")
    display_guitars(guitars)


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

main()