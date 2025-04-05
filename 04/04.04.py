def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
def isPerfect(num):
    t = 0
    for i in range(1, num):
        if num % i:
            t += i
    if t == num:
        return True
    return False
def isArmstrong(num):
    stNum = str(num)
    t = 0
    for i in stNum:
        t += int(i) ** len(stNum)
    if t == num:
        return True
    return False
def isPal(num):
    stNum = str(num)
    stRevNum = reversed(stNum)
    if stNum == stRevNum:
        return True
    return False
def isAutomorphic(num):
    stNum = str(num**2)
    if stNum.endswith(str(num)):
        return True
    return False

n = int(input("Enter number: "))

print(f"""
isPrime = {isPrime(n)}
isPerfect = {isPerfect(n)}
isArmstrong = {isArmstrong(n)}
isPal = {isPal(n)}
isAutomorphic = {isAutomorphic(n)}
""")
