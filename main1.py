def NWD(x, y):
    while(y>0):
        z=x%y
        x=y
        y=z
    print(x)
    return x
x=int(input("X: "))
y=int(input("Y: "))
NWD(x,y)
