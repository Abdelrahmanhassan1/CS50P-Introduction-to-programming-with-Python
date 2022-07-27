import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

if sys.argv[1].split(".")[1] != "csv" or sys.argv[2].split(".")[1] != "csv":
    sys.exit("Not a CSV file")

try:
    firstNames = []
    lastNames = []
    houses = []

    # reading the old data
    with open(file_name, "r", newline="") as old_file:

        reader_file = csv.DictReader(old_file)

        for row in reader_file:

            # splitting the name
            last, first = row['name'].strip().split(",")
            firstNames.append(first.strip())
            lastNames.append(last.strip())
            houses.append(row['house'])

    print(firstNames, lastNames, houses)
    with open("after.csv", "w") as new_file:

        fieldNames = ['first', 'last', 'house']

        writer_file = csv.DictWriter(new_file, fieldnames=fieldNames)


except FileNotFoundError:

    sys.exit(f"Could not read {file_name}")
