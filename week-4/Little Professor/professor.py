from random import randint


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        number_of_tries = 0
        x = generate_integer(level)
        y = generate_integer(level)
        if is_valid_for_first_check(x, y):
            score += 1
        else:
            while True:
                number_of_tries += 1
                if number_of_tries < 3:
                    try:
                        print("EEE")
                        result = int(input(str(x) + " + " + str(y) + " = "))
                        if result == x+y:
                            break
                    except ValueError:
                        print("EEE")
                else:
                    print(f"{x} + {y} = {x+y}")
                    break

    print(f"Score: {score}")


def get_level():

    while True:

        try:

            level = int(input("Level: "))

            if level in range(1, 4):

                return level

        except ValueError:

            continue


def generate_integer(level):

    if level == 1:
        return (randint(0, 10))
    elif level == 2:
        return (randint(10, 99))
    else:
        return (randint(100, 999))


def is_valid_for_first_check(number1, number2):
    try:
        result = int(input(str(number1) + " + " + str(number2) + " = "))
        if number1 + number2 == result:
            return True
        return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
