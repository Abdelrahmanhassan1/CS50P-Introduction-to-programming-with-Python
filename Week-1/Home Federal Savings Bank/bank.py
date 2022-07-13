# greeting = input("Greeting: ").lower().strip().replace("submit50 cs50/problems/2022/python/bank", "").split()
# cost = 0
# if greeting[0][0] == "h":
#     if greeting[0] == "hello":
#         cost = 0
#     else:
#         cost = 20
# else:
#     cost = 100

# print(f"${cost}")


greeting = input("Greeting: ").lower().strip()

if "hello" in greeting:
    cost = 0
elif "h" == greeting[0]:
    cost = 20
else:
    cost = 100
print(f"${cost}")
