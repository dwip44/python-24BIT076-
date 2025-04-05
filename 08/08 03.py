s = set()
for i in range(5):
    nm = input("Enter name: ")
    s.add(nm)

print("Modifying...")
nm = input("Enter name to edit: ")
s.discard(nm)
nm = input("Enter new name: ")
s.add(nm)

print(s)

for i in range(2):
    nm = input("Enter name to delete: ")
    s.discard(nm)

print(s)
