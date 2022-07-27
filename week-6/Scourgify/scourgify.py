import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

if sys.argv[1].split(".")[1] != "csv" or sys.argv[2].split(".")[1] != "csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[2], "w") as new_file:

        writer_file = csv.writer(new_file)

        with open(file_name, "r", newline="") as old_file:

            reader_file = csv.reader(old_file)

            for index, row in enumerate(reader_file):
                # getting the header of the new file
                if index == 0:
                    writer_file.writerow(['first', 'last', 'house'])
                    continue

                # splitting the name
                last, first = row[0].strip().split(",")

                # modifying the rows of the csv file
                new_row = [first.strip(), last.strip(), row[1]]

                writer_file.writerow(new_row)

except FileNotFoundError:

    sys.exit(f"Could not read {file_name}")
