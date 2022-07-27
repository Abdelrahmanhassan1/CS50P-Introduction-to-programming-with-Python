from random import randint
import sys


def game():
    while True:
        try:
            # Start
            level = int(input("Level: "))

            random_number = randint(1, level)

            while True:
                # Start
                guess = int(input("Guess: "))

                if guess < 0:
                    continue

                if guess == random_number:
                    sys.exit("Just right!")

                elif guess > random_number:
                    print("Too large!")

                elif guess < random_number:
                    print("Too small!")

        except ValueError:
            pass


game()
