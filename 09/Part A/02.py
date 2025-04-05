def compute(n):
    return n + int(str(n)*2) + int(str(n)*3) + int(str(n)*4)

for i in range(4, 8):
    print(compute(i))
