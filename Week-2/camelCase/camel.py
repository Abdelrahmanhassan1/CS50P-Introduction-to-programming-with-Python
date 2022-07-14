camelCaseName = input("camelCase: ")

# looping iover the name
for letter in camelCaseName:

    # check if the letter is capital
    if(letter.isupper()):
        print("_", end="")

    print(letter.lower(), end="")

    # note end="" must be used as default will make a new line

print()
