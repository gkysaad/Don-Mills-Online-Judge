word = input()
length = 0
for i in range(len(word)):
    for i2 in range(len(word)):
        if i2 >= i:
            newword = word[i:i2+1]
            if newword == newword[::-1]:
                if i2+1-i > length:
                    length = i2+1-i
                
print(length)
    
