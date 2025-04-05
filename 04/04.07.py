def fact(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

def ncr(n,r):
    return fact(n)/(fact(n-r) * fact(r))

def npr(n,r):
    return fact(n)/(fact(n-r))

n = int(input("n : "))
r = int(input("r : "))

print(f"{n}C{r} = {ncr(n,r)}")
print(f"{n}P{r} = {npr(n,r)}")
