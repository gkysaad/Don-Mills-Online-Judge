num1 = int(input())
scount = 0
tcount = 0
for i in range(num1):
    line = input().lower()
    for i in range(len(line)):
        if line[i] == "s":
            scount += 1
        elif line[i] == "t":
            tcount += 1
if tcount > scount:
    print("English")
else:
    print("French")
