import math

def lcm(x, y):
    return abs(x*y)//math.gcd(x,y)

A = int(input())
B = int(input())
X = int(input())

lcm = lcm(A, B)

counter = X//lcm

if lcm != 1:
    counter += 1

print(counter)
