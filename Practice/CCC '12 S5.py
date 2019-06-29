import pprint
pp = pprint.PrettyPrinter(indent=4)

R, C = list(map(int, input().split(" ")))

main = []
cats = []

for i in range(R + 2):
    main.append([])
    cats.append([])
    for i2 in range(C + 2):
        main[i].append(0)
        cats[i].append(0)

ncats = int(input())

for cat in range(ncats):
    x, y = list(map(int, input().split(" ")))
    cats[x][y] = 1

main[1][1] = 1

for x in range(1, R+1):
    for y in range(1, C+1):
        if cats[x][y] == 1:
            continue
        else:
            main[x][y] += main[x-1][y] + main[x][y-1]

print(main[R][C])
