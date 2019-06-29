counter = int(input())
probability = 1.0
for i in range(counter):
    eg, pg = input().split(" ")
    prob = (float(pg)-float(eg))/float(pg)
    probability = probability*prob

print(round(probability, 10**6))
    
