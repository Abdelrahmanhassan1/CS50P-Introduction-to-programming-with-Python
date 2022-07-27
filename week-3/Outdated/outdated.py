months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():

    while True:
        outdate = input("Date: ")

        if "/" in outdate:
            try:
                month, day, year = [int(num) for num in outdate.split("/")]
                # check valid Date
                if month > 12 or month < 1 or day > 31 or day < 1 or year < 999:
                    continue

                return (f"{year:04}-{month:02}-{day:02}")
            except ValueError:
                continue

        elif outdate.split(" ")[0] in months and "," in outdate.split(" ")[1]:
            month = months.index(outdate.split(" ")[0]) + 1
            day = int(outdate.split(" ")[1].replace(",", ""))
            year = int(outdate.split(" ")[2])
            # check valid Date
            if month > 12 or month < 1 or day > 31 or day < 1 or year < 999:
                continue

            return (f"{year:04}-{month:02}-{day:02}")


new_date = main()
print(new_date)
