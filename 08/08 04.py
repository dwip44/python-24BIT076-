s = {"Aarnav", "Abhinav", "Aryan", "Aaditya","Bivya", "Barth", "Bet", "Baan"}
A = set()
B = set()

for i in s:
    if i.startswith("A"):
        A.add(i)
    elif i.startswith("B"):
        B.add(i)

print(f"s = {s}")
print(f"A = {A}")
print(f"B = {B}")
