letr = ""
letterNum = 0
placementNum = 0
plusTen = 0
plusOne = 0
readyLetters = []
translation = []
startOfWord = ["w","W"]
text = input()
words = text.split(" ")
letters = list(text)
bannedLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','x','y','z']
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letterEndsAt = []
for x in range(len(letters)):
    if letters[x] in bannedLetters:
        raise Exception("This is not fluent Fallian...")
for x in range(len(letters)):
    if letters[x] in startOfWord:
        if letters[x].islower():
            for y in range(x+1,len(letters)):
                if letters[y]=="o":
                    plusOne+=1
                elif letters[y]=="O":
                    plusTen+=1
                elif letters[y].lower()=="w":
                    break
            translation.append(alph[(plusTen*10)+plusOne-1])
        elif letters[x].isupper():
            for y in range(x+1,len(letters)):
                if letters[y]=="o":
                    plusOne+=1
                elif letters[y]=="O":
                    plusTen+=1
                elif letters[y].lower()=="w":
                    break
            translation.append(alph[(plusTen*10)+plusOne-1].capitalize())
    elif letters[x].lower()=="o":
        pass
    else:
        translation.append(letters[x])
    plusOne = 0
    plusTen = 0
print("".join(translation))

