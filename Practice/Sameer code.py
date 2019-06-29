import sys
import math
all_data = [int(input())]
while all_data[len(all_data)-1] != 0:
    inp = int(input())
    all_data.append(inp)
#all_data = sys.stdin.read().split('\n')
check = 0
for i in range(len(all_data)):
    all_data[i] = int(all_data[i])
for j in range(len(all_data)):
    check = 0
    x = math.floor(math.sqrt(all_data[j]))
    if (all_data[j] == 0):
        exit()
    for k in range(math.floor(math.sqrt(all_data[j])),0,-1):
        if(all_data[j]%k == 0) and (check ==0):
            per = 2*k+2*int(all_data[j]/k)
            print("Minimum perimeter is "+str(per)+" with dimensions "+str(k)+" x "+str(int(all_data[j]/k)))
            check = 1
            break
