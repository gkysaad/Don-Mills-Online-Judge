quarters = int(input())
machine = 1
m1 = int(input())
m2 = int(input())
m3 = int(input())
counts = 0
while quarters > 0:
    quarters -= 1
    if machine == 1:
        m1 += 1
        if m1%35 == 0:
            quarters += 30
        machine = 2
    elif machine == 2:
        m2 += 1
        if m2%100 == 0:
            quarters += 60
        machine = 3
    else:
        m3 += 1
        if m3%10 == 0:
            quarters += 9
        machine = 1
    counts += 1
print("Martha plays", counts, "times before going broke.")
