def isSame(st1, st2):
    if len(st1) > len(st2):
        for i in range(0, len(st1)):
            if st2 == st1[:i]:
                return True
    elif len(st2) > len(st1):
        for i in range(0, len(st2)):
            if st1 == st2[:i]:
                return True
    elif st2 == st1:
        return True
    return False
st1 = input("String 1: ")
st2 = input("String 2: ")

if isSame(st1,st2):
    print("String is present in another")
else: 
    print("String is not present in another")
