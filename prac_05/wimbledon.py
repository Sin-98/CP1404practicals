"""
Wimbledon
Estimate: 35 minutes
Actual:  29  minutes
"""

FILENAME = "wimbledon.csv"

def main():
    """Read the file, process the data and display processed information about Wimbledon champions and countries."""
    records = get_records()
    champion_to_count, countries = process_records(records)
    display_records(champion_to_count, countries)

def display_records(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(",".join(sorted(countries)))


def process_records(records):
    """Create dictionary of champions and set of countries from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        champion_to_count[record[2]] = champion_to_count.get(record[2], 0) + 1
    return champion_to_count, countries


def get_records():
    """Get records from file and change into list of lists."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()