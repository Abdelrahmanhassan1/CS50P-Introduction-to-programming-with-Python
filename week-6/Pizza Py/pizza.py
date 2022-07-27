import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

if file_name.split(".")[1] != "csv":
    sys.exit("Not a CSV file")

try:
    with open(file_name, "r", newline="") as f:

        csv_file = csv.reader(f)

        table = []

        for index, row in enumerate(csv_file):
            if index == 0:
                header = row
                continue
            table.append(row)

        print(tabulate(table, header, tablefmt="grid"))


except FileNotFoundError:

    sys.exit("File does not exist")
