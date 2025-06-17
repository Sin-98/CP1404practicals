"""
Wimbledon
Estimate: 35 minutes
Actual:    minutes
"""

FILENaME = "wimbledon.csv"

def main():
    records = []
    with open(FILENaME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    print(records)

    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        champion_to_count[record[2]] = champion_to_count.get(record[2], 0) + 1
    print(champion_to_count)
    print(countries)

    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(",".join(sorted(countries)))

main()