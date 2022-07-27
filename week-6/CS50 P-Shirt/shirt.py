import sys
from PIL import Image
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]
extensions = ['png', 'jpg', 'jpeg']

if sys.argv[1].split(".")[1] not in extensions or sys.argv[2].split(".")[1] not in extensions:
    sys.exit("Invalid output")

if sys.argv[1].split(".")[1] in extensions:
    if sys.argv[2].split(".")[1] != sys.argv[1].split(".")[1]:
        sys.exit("Input and output have different extensions")


# try:


# except FileNotFoundError:

#     sys.exit(f"Input does not exist")
