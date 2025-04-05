def fibo(n):
    one = 0
    two = 1
    count = 0
    while count < n:
        print(one )
        sum = one+ two
        one = two
        two = sum
        count += 1

n = int(input("Enter n: "))
fibo(n)
