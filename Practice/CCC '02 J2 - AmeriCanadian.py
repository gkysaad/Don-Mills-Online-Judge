word = input()
vowels = ['a','e','i','o','u','y']
while word != "quit!":
    if "or" in word:
        orspot = word.index("or")
        consonant = False
        if word[orspot-1] not in vowels:
            consonant = True
        if consonant and orspot > 1 and orspot+2 == len(word):
            word = word.split("or")
            word = word[0] + "our" + word[1]
        print(word)
        word = input()
