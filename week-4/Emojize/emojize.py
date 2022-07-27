from emoji import emojize

text = input("Input: ")

print("Output: ", end="")

print(emojize(text, language='alias'))
