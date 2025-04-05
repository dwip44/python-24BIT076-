def toUpper(st):
    up = ""
    for i in range(len(st)):
        print(ord(st[i]))
        if ord(st[i]) >= 97 :
            # st[i] is in lowercase
            up += chr(ord(st[i]) - 32)
        else: 
            up += st[i]            
    return up
def toLower(st):
    low = ""
    for i in range(len(st)):
        print(ord(st[i]))
        if ord(st[i]) <= ord("Z") :
            # st[i] is in uppercase
            low += chr(ord(st[i]) + 32)
        else: 
            low += st[i]            
    return low
def toToggle(st):
    tog = ""
    for i in range(len(st)):
        print(ord(st[i]))
        if ord(st[i]) >= 97 :
            # st[i] is in lowercase
            tog += chr(ord(st[i]) - 32)
        elif ord(st[i]) <= ord("Z") :
            # st[i] is in uppercase
            tog += chr(ord(st[i]) + 32)
        else: 
            tog += st[i]            
    return tog

st = input("Enter a string: ")
print(f"Lowercase : {toLower(st)}")
print(f"Uppercase : {toUpper(st)}")
print(f"Togglecase : {toToggle(st)}")
