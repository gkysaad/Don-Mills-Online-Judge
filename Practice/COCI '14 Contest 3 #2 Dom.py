N, M, P = input().split(" ")
favs = []
hates = []
index = []
counter = 0
isin = False
for i in range(int(N)):
    l, h = input().split(" ")
    favs.append(l)
    hates.append(h)
while P in hates:
    isin = True
    ind = hates.index(P)
    if ind in index:
        isin = False
        break
    else:
        index.append(ind)
        P = favs[ind]
        counter += 1
        
if not isin:
    print(-1)
else:
    print(counter)
