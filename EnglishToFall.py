text = input()
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
words = text.split(" ")
letters = list(text)
isUpper = []
translatedLetters = []
translatedWords = None
for x in range(len(letters)):
    if letters[x].isupper():
        isUpper.append(True)
    else:
        isUpper.append(False)
for y in range(len(letters)):
    for z in range(len(alph)):
        if letters[y].lower() == alph[z]:
            zz = z+1
            if isUpper[y] == True:
                translatedLetters.append("W"+"O"*(int((zz-(zz%10))/10))+"o"*(zz%10))
            elif isUpper[y] == False:
                translatedLetters.append("w"+"O"*(int((zz-(zz%10))/10))+"o"*(zz%10))
            zz = 0
        elif letters[y].lower() not in alph and alph[z]=='z':
            translatedLetters.append(letters[y])
translatedWords = "".join(translatedLetters)
print(translatedWords)


    

            
