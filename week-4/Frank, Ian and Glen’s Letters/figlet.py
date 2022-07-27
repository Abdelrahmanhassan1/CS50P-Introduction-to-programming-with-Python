import sys

import random

from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

options = ["-f", "--font"]


def main():

    if len(sys.argv) == 1:
        font = random.choice(fonts)
        sys.exit()

    elif len(sys.argv) > 1:

        if len(sys.argv) == 2:
            sys.exit("Invalid usage")

        if sys.argv[1] in options:

            if sys.argv[2] in fonts:

                font = sys.argv[2]
                figlet.setFont(font=font)
                text = input("Input: ")
                print(figlet.renderText(text))
                sys.exit()

        sys.exit("Invalid usage")


main()
