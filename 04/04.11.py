def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
    
def sin(n):
    val = 0
    for i in range(0,11, 2):
        if i %2 == 0:
            val += n**(i + 1)/fact(i+1)
        else: 
            val -= n**(i + 1)/fact(i+ 1)
    return val

print(sin(3.14))
