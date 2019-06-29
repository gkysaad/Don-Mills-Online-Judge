type1 = input()
x1,y1,z1 = input().split(" ")
x1 = float(x1)
y1 = float(y1)
z1 = float(z1)
x2,y2,z2 = input().split(" ")
x2 = float(x2)
y2 = float(y2)
z2 = float(z2)
if type1 == "Multiply":
    newx = x1*x2
    newy = y1*y2
    newz = z1*z2
elif type1 == "Screen":
    newx = 1-(1-x1)*(1-x2)
    newy = 1-(1-y1)*(1-y2)
    newz = 1-(1-z1)*(1-z2)
else:
    if x1 < 0.5:
        newx = 2*x1*x2
    else:
        newx = 1-2*(1-x1)*(1-x2)
    if y1 < 0.5:
        newy = 2*y1*y2
    else:
        newy = 1-2*(1-y1)*(1-y2)
    if z1 < 0.5:
        newz = 2*z1*z2
    else:
        newz = 1-2*(1-z1)*(1-z2)

print(str(newx) + " " + str(newy) + " " + str(newz))
    
    
