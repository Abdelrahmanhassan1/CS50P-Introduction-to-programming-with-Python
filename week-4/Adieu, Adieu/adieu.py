import inflect

p = inflect.engine()

names_list = []
song = "Adieu, adieu, to "

while True:
    try:
        name = input("Name: ")
        names_list.append(name)

    except EOFError:
        print()
        break

names_styled = p.join(names_list)
print(song + names_styled)
