import collections

englishLettersCommonDict = {"E":12.7, "T":9.06, "A":8.17, "O":7.51, "I":6.97, "N":6.75, "S":6.33, "H":6.09, "R":5.99, "D":4.25, "L":4.03, "C":2.78, "U":2.76, "M":2.41, "W":2.36, "F":2.23, "G":2.02, "Y":1.97, "P":1.93, "B":1.29, "V":0.98, "K":0.77, "J":0.15, "X":0.15, "Q":0.1, "Z":0.07}

englishLettersCommon = lambda letter: englishLettersCommonDict[letter]

def caesarCipherEncryp(string, numb):
    newString = list(string)
    Numb = 0
    listString = " "
    listString = list(string)
    for i in range(len(listString)):
        if listString[i].isalpha() == False:
            newString[i] = listString[i]
        elif listString[i].upper() == listString[i]:
            Numb = ord(listString[i])
            while Numb + numb > 90:
                if Numb + numb > 90:
                    Numb -= 26
            newString[i] = chr(Numb + numb)
        else:
            Numb = ord(listString[i])
            while Numb + numb > 122:
                if Numb + numb > 122:
                    Numb -= 26
            newString[i] = chr(Numb + numb)
    return "".join(newString)
    
def ModdedCaesarCipherCrack(string):
    best = 0
    best2 = 0
    count = 0
    newStr = 0
    newStr = string
    for i in range(26):
        newStr = caesarCipherEncryp(newStr, 1)
        count = 0
        for j in range(len(string)):
            if newStr[j].isalpha() == True:
                count += englishLettersCommon(newStr[j])
        if count > best:
            best = count
            best2 = i
    return best2

ciphertext = ""
ciphertext = ciphertext.upper().replace(" ","")
key_length = 0
for i in range(1, 20):
    do_break = False
    for j in range(i):
        current_ciphertext = ciphertext[::i]
        top1 = (ord(collections.Counter(current_ciphertext).most_common()[0][0])-65)
        top2 = (ord(collections.Counter(current_ciphertext).most_common()[1][0])-65)
        if (top2-top1)%26 == 15:
            key_length = i
            do_break = True
            break
    if do_break:
        break
if i == 19:
    raise SystemExit
key = ""
for i in range(key_length):
    key += chr(26-caesarCipherCrack(ciphertext[i::key_length])+64)
print(key)
