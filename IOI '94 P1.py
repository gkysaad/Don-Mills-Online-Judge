rows = int(input())

original = []

for i in range(rows):
    original.append(input().split(" "))
    original[i] = list(map(int, original[i]))

sums = [[original[x][y] for y in range(len(original[x]))] for x in range(len(original))]

for i in range(rows - 1):
    for j in range(len(sums[i])):
        current = sums[i][j]
        sums[i+1][j] = max(current + original[i+1][j], sums[i+1][j])
        sums[i+1][j+1] = max(current + original[i+1][j+1], sums[i+1][j+1])

print(max(sums[rows-1]))
