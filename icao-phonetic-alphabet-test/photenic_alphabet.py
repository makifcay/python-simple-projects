from random import shuffle

phoneticDict = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
                'G': 'Golf', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 
                'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 
                'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}

#Shuffle method cannot be used for dict, so we need to convert.
phoneticDictConvert = list(phoneticDict.items())
shuffle(phoneticDictConvert)
phoneticDict = dict(phoneticDictConvert)

trueCount = 0
falseCount = 0

for symbol, word in phoneticDict.items():
    
    tryingCount = 3

    while(True):
        if tryingCount == 0:
            falseCount += 1
            print("\nAnswer = {}\n".format(word))
            break

        #print("\n{} =".format(symbol), end = ' ')
        answer = input("\n{} = ".format(symbol))

        if answer == word or answer == word.lower():
            print("True", end = '\n')
            trueCount += 1
            break

        else:
            tryingCount -= 1
            print("False")

print("\nTrue = {}\nFalse = {}".format(trueCount,falseCount))