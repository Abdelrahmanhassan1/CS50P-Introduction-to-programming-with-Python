def main():
    time = convert(input("Time: ").strip())
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    """
    Convert a time in the format of HH:MM to a number.
    """
    hour, minute = time.split(':')
    return (int(hour) + int(minute)/60).__round__(2)


if __name__ == "__main__":
    main()
