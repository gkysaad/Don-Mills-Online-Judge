import math

def nCr(n, r):
    return int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

all1 = int(input())
names = input().split(" ")
continuos = False
multiples = []
counter = all1
for i in range(all1):
    names[i] = names[i][0].lower()
    if i != 0:
        if names[i] == names[i-1]:
            if continuos:
                multiples[len(multiples)-1] += 1
            else:
                continuos = True
                multiples.append(2)
        else:
            continuos = False
for i in range(len(multiples)):
    for i2 in range(2, multiples[i]+1):
        counter += nCr(multiples[i],i2)

print(counter%1000000007)        
