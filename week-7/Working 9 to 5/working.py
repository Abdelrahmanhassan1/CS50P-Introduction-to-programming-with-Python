import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    matching = re.search(
        r'(\d+):?(\d+)? (AM|PM) to (\d+):?(\d+)? (AM|PM)', s)
    #        1     2       3          4     5       6

    if matching:
        # check for valid hours:
        if int(matching[1]) < 0 or int(matching[1]) > 12:
            raise ValueError

        elif int(matching[4]) < 0 or int(matching[4]) > 12:
            raise ValueError

        # check for valid minutes
        if matching[2]:
            if int(matching[2]) < 0 or int(matching[2]) > 59:
                raise ValueError

        if matching[5]:
            if int(matching[5]) < 0 or int(matching[5]) > 59:
                raise ValueError

        # convert to new dates
        if matching[3] == "AM":
            if matching[1] == "12":
                first_hours = str(0).zfill(2)
            else:
                first_hours = str(matching[1]).zfill(2)

            if matching[2]:
                first_minutes = str(matching[2]).zfill(2)
            else:
                first_minutes = str(0).zfill(2)

        elif matching[3] == "PM":
            if matching[1] == "12":
                first_hours = str(int(matching[1])).zfill(2)
            else:
                first_hours = str(int(matching[1]) + 12).zfill(2)
            if matching[2]:
                first_minutes = str(matching[2]).zfill(2)
            else:
                first_minutes = str(0).zfill(2)

        if matching[6] == "AM":
            if matching[4] == "12":
                last_hours = str(0).zfill(2)
            else:
                last_hours = str(matching[4]).zfill(2)

            if matching[5]:
                last_minutes = str(matching[5]).zfill(2)
            else:
                last_minutes = str(0).zfill(2)

        elif matching[6] == "PM":
            if matching[4] == "12":
                last_hours = str(int(matching[4])).zfill(2)
            else:
                last_hours = str(int(matching[4]) + 12).zfill(2)
            if matching[5]:
                last_minutes = str(matching[5]).zfill(2)
            else:
                last_minutes = str(0).zfill(2)

        return first_hours + ":" + first_minutes + " to " + last_hours + ":" + last_minutes
    else:
        raise ValueError


if __name__ == "__main__":
    main()
