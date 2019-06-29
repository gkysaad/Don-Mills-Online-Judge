N, D = input().split(" ")
N = int(N)
D = abs(int(D))
incr = input().split(" ")
largest = 0
for i in range(N):
    incr[i] = int(incr[i])
    if D%incr[i] == 0 and incr[i] > largest:
        largest = incr[i]

if largest > 0:
    print(int(D/largest))
else:
    print("This is not the best time for a trip.")
