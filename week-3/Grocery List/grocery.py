grocery_list = {}

while True:
    try:
        item = input().upper()
        # Here we want to get the number of purshaing this item and in case it's not in the list,
        # we want to add it with initial value = 0.
        grocery_list[item] = grocery_list.get(item, 0) + 1

    except KeyError:
        pass

    except (EOFError):
        print()
        for key in sorted(grocery_list.keys()):
            print(f"{grocery_list[key]} {key}")
        break
