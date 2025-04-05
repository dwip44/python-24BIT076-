st = input("Enter string: ")
countChr = 0
countNum = 0

for i in st:
    if i.isnumeric():
        countNum += 1
    if i.isalpha():
        countNum += 1

print("Alphabets: ", countChr)
print("Numbers: ", countNum)
