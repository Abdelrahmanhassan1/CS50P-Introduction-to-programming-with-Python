import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    groups = re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip)

    if groups:

        for i in range(1, 5):

            if int(groups[i]) in range(0, 256):
                continue
            else:
                return False

        return True

    return False


if __name__ == "__main__":
    main()
