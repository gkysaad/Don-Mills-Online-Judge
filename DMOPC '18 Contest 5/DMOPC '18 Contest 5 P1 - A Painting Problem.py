N, M, K = input().split(" ")
N = int(N)
M = int(M)
binN = format(N, 'b')
binM = format(M,'b')
binN = binN[::-1]
binM = binM[::-1]
blue = 0
purple = 0
#print(binN, binM)
if len(binN) < len(binM):
    for i in range(len(binN)):
        if binN[i] == binM[i]:
            purple += 1
        else:
            blue += 1
    diff = int(K) - len(binN)
    for i2 in range(diff):
        if binM[i+i2] != 0:
            blue += 1
        else:
            purple += 1
else:
    for i in range(len(binM)):
        if binN[i] == binM[i]:
            purple += 1
            #print(i)
        else:
            blue += 1
    diff = int(K) - len(binM)
    for i2 in range(diff):
        if binN[i+i2] != 0:
            blue += 1
        else:
            purple += 1

print(str(blue) + " " + str(purple))
    
