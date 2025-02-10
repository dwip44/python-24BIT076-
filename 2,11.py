x1=int(input("x1 is"))
x2=int(input("x2 is"))
x3=int(input("x3 is"))
y1=int(input("y1 is"))
y2=int(input("y2 is"))
y3=int(input("y3 is"))
a=(x2-x1)/(y2-y1)
b=(x3-x2)/(y3-y2)
c=(x1-x3)/(y1-y3)
if(a==b==c):
    
    print("the three points fall on one straight line")
else:
    print("the points do not lie on a straight line")