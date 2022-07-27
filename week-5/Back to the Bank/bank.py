
def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        cost = 0
    elif "h" == greeting[0]:
        cost = 20
    else:
        cost = 100

    return cost


if __name__ == "__main__":
    main()
