num = int(input())
computers = []
ratings = []
for i in range(num):
    inp = input().split(" ")
    computers.append(inp[0])
    rating = 2*int(inp[1]) + 3*int(inp[2]) + int(inp[3])
    ratings.append(rating)

new = list(zip(ratings, computers))
new.sort()
output = [new[-1][1]]
vals = [new[-1][0]]
if len(new) > 1:
    for i in range(len(new)-2):
        i += 1
        if new[-i][0] == new[-i-1][0] or i == 1:
            output.append(new[-i-1][1])
            vals.append(new[-i-1][0])
        output.sort()
tosort = list(zip(vals,output))
tosort.sort()
if tosort[-1][0] != tosort[0][0]:
    big = tosort[0][0]
    small = tosort[-1][0]
    bigl =[]
    smalll =[]
    for i in range(len(tosort)):
        if tosort[i][0] == big:
            bigl.append(tosort[i][1])
        else:
            smalll.append(tosort[i][1])
bigl.sort()
smalll.sort()
print(bigl[0])
if len(bigl) > 1:
    print(big1[1])
else:
    print(smalll[0])
