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

main()