import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

if file_name.split(".")[1] != "py":
    sys.exit("Not a Python file")

try:
    with open(file_name, "r") as f:

        complexity = 0

        file_lines = f.readlines()

        # removing new line space at the end of the line
        lines = [line.rstrip() for line in file_lines]
        # print(len(lines))

        # removing white spaces between words
        lines = [line.strip() for line in lines]

        # removing empty lines from the lines list
        lines = list(filter(None, lines))
        # print(len(lines))

        for line in lines:
            if line[0] != "#":
                complexity += 1

        print(complexity)

except FileNotFoundError:
    sys.exit("File does not exist")
