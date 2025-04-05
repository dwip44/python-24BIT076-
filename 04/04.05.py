for i in range(3, 31):
    for j in range(3,31):
        a = str((i**2 + j**2)**0.5)
        if a.isdigit():
            print(f"{i} {j} {(i**2 + j**2)**0.5}")
