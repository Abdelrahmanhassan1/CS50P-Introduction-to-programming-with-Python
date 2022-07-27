import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s.startswith('<iframe'):
        matches = re.search('https?://(?:www\.)?youtube\.com/embed/(\w+)', s)
        if matches:
            new_link = f"https://youtu.be/{matches[1]}"
            return new_link


if __name__ == "__main__":
    main()
