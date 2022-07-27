
def main():
    vanity_plate = input("Plate: ")
    if is_valid(vanity_plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # First check
    if len(plate) > 6 or len(plate) < 2:
        return False
    # Second Check for the first two letters
    if not(plate[0:2].isalpha()):
        return False

    # Third Check for the periods, spaces, or punctuations
    if not(plate.isalnum()):
        return False

    # Fourth Check for the first occurence of number to not be zero
    if not(plate.isalpha()):
        # then there are some number in the plate
        for index, char in enumerate(plate[2:]):
            if char.isnumeric():
                if int(char) == 0:
                    return False
                # Here we need to check for middle numbers after the first occurence of digit
                for index2 in range(index+2, len(plate)):
                    if plate[index2].isalpha():
                        return False
            break

    return True


if __name__ == "__main__":
    main()
