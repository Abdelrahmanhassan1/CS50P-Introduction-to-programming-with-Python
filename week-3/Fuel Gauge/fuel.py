

def main():
    while True:
        try:
            fraction = input("Fraction: ")

            x, y = [int(num) for num in fraction.split("/")]

            if x > y:
                continue

            if (x/y)*100 <= 1:
                return "E"

            if (x/y)*100 >= 99:
                return "F"

            return (f"{int(round((x / y) * 100))}%")

        except (ZeroDivisionError, ValueError):

            pass


result = main()
print(result)
