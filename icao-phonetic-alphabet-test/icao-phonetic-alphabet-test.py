
itu_phonetic_dict = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
                     'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
                     'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor',
                     'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}
"""
for x in itu_char_dict:
    print(x)
    print(itu_char_dict[x])
"""

for x, y in itu_phonetic_dict.items():
    print("{} - {}".format(x, y))

true_count = 0
false_count = 0
trying_count = 3

for letter, code in itu_phonetic_dict.items():

    while True:
        print("{} = ".format(letter))
        answer = input()

        if answer == code:
            true_count = true_count + 1
            print("True")
            break

        else:
            false_count = false_count + 1
            print("False")
            break

            """
                    while True:
            if trying_count == 0:
                print("False")
                false_count = +1
                trying_count = 3
                break
            print("Try again")
            trying_count = -1
            break
            """

print("True: {}\nFalse: {}".format(true_count, false_count))
