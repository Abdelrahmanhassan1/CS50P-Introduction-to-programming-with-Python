text = input("Input: ")

vowels = ["a", "e", "o", "i", "u"]

print("Output: ", end="")

# looping on the string
for char in text:

    if char.lower() in vowels:
        continue

    print(char, end="")

print()
