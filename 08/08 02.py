from random import randint

s = set()

for i in range(10):
    s.add(randint(15,45))
print(s)

count = 0
for i in s.copy():
    if i < 30:
        count+=1
    if i > 35:
        s.discard(i)

print(f"Count of numbers less than 30 = {count}")
print(s)
