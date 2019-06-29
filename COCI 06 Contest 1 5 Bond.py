N = int(input())
lines = []
iavail =[]

for i in range(N):
    line = list(map(float, input().split(" ")))
    lines.append(line)
    iavail.append(i)

second = [[lines[x][y] for y in range(N)] for x in range(N)]

for i in range(N):
    for j in range(N):
        avail = iavail.copy()
        avail.remove(j)
        prob = lines[i][j]/100.0
        for k in range(i+1,N):
            for j2 in range(N):
                if 
            
            if j != 0:
                second[i+1][k] = max(second[i][j]/100.0 * lines[i+1][k]/100.0, second[i+1][k])
            else:
                second[i+1][k] = second[i][j]/100.0 * lines[i+1][k]/100.0
print(second)
