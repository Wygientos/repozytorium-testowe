def NWD(x, y):
    while(y>0):
        z=x%y
        x=y
        y=z
    print(x)
    return x
x=int(input("X: "))
y=int(input("Y: "))
if(x>0):
    if(y>0):
        NWD(x,y)
    else:
        input("blad")
