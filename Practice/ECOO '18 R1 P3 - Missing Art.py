import sys
nextin = "*"
while nextin == "*":
    N,X,Y,Z = input().split(" ")
    N = int(N)
    X = int(X)
    Y = int(Y)
    Z = int(Z)
    codes = []
    broken = []
    for i in range(N):
        code = input()
        newcode = ""
        for i2 in range(len(code)):
            current = int(code[i2])
            if current == 0:
                newcode = newcode + str(Z)
            elif current%2 == 0:
                current += X
                newcode = newcode + str(current)
            else:
                current -= Y
                if current < 0:
                    current = 0
                newcode = newcode + str(current)
        codes.append(newcode)
    A = input()
    for i in range(N):
        answer = input()
        if answer != codes[i]:
            broken.append(i+1)
    if len(broken) == 0:
        print("MATCH")
    else:
        print("FAIL: ", end="")
        for i in range(len(broken)):
            if i != 0:
                print(","+str(broken[i]), end="")
            else:
                print(str(broken[i]), end="")
        print()
    nextin = input()

            
        
            
