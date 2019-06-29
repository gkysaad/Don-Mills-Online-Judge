candidates, votenum = input().split(" ")
cand = []
voters = []
first = []
comb = [(0,0), (1,1)]
for i in range(int(candidates)):
    cand.append(input())
for i in range(int(votenum)):
    inp = input().split(" ")
    numvotes = int(inp[0])
    percand = []
    for i in range(numvotes):
        percand.append(inp[i+1])
    voters.append(percand)
while len(comb) > 1:
    votes = list(cand)
    first = []
    for i in range(len(voters)):
        first.append(voters[i][0])
        #print(voters)
        #print(voters[i])
    for i in range(len(cand)):
        num = first.count(cand[i])
        #print(cand[i])
        #print(first)
        #print(num)
        votes[i] = num
    comb = list(zip(votes, cand))
    comb.sort()
    #print(comb)
    if len(comb) > 1:
        remove = comb[0][1]
        numr = int(comb[0][0])
        removed = 0
        topop = [] 
        for i in range(len(first)):
            if first[i] == remove:
                if removed == numr:
                    break
                #print(first)
                voters[i].pop(0)
                removed += 1
                #print(voters[i])
            if len(voters[i]) < 1:
                topop.append(i)
        for i in topop:
            voters.pop(i)
        cand.pop(cand.index(remove))
print(comb[0][1])

    
        
        
        
    
