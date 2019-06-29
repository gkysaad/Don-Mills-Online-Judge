size, evnum = input().split(" ")
size = int(size)
grid = list(range(int(size)))
for i in range(int(size)):
    grid[i] = list(range(size))
for i in range(int(size)):
    for j in range(int(size)):
        grid[j][i] = 0
for i in range(int(evnum)):
    event = input().split(" ")
    x = int(event[1]) - 1
    y = int(event[2]) - 1
    if int(event[0]) == 1:
        for i in range(int(size)):
            grid[i][x] = 1 - grid[i][x]
            grid[y][i] = 1 - grid[y][i]
        grid[y][x] = 1 - grid[y][x]
    else:
        print(grid[y][x])
    
    
