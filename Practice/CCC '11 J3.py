tlist = [int(input()), int(input())]

while True:
    diff = abs(tlist[len(tlist)-1] - tlist[len(tlist)-2])
    tlist.append(diff)
    if tlist[len(tlist)-2] < diff:
        print(len(tlist))
        break
    
