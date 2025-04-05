a = input("Enter string: ")
count = 0
for i in a.lower():
    if i == "a" or i == "e" or i == "i" or i== "o" or i=="u":
        count += 1
print(f"No. of vowels = {count}")
