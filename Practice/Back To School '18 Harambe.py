line1 = input()
line2 = input()
K = int(input())
changes = 0
override = False
for i in range(len(line1)):
    if line1[i] != line2[i]:
        changes += 1
        if line1[i] == " " or line2[i] == " ":
            override = True
if changes <= K and not override:
    print("Pagiarized")
else:
    print("No plagairism")
    
