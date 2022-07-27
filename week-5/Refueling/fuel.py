def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent)+"%")


def convert(fraction):
    num, denum = fraction.split("/")
    while True:
        try:
            num = int(num)
            denum = int(denum)
            result = num/denum
            if num > denum:
                continue
            else:
                percentage = int(round((num/denum) * 100))
                return percentage
        except ValueError:
            raise ValueError("x and y arenot integers")
        except ZeroDivisionError:
            raise ZeroDivisionError("cant't divide on zero")


def gauge(percentage):
    if percentage:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return str(percentage)
    else:
        return


if __name__ == "__main__":
    main()
