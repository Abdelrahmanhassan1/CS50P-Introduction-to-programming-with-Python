remain = 50

while remain > 0:

    print(f"Amount due: {remain}")

    value = int(input("Insert Coin: "))

    if value in [25, 10, 5]:
        remain -= value


# if remain < 0:
#     print(f"Change Owed: {remain * -1}")
# else:
#     print("Change Owed: 0")

print(f"Change Owed = {abs(remain)}")
