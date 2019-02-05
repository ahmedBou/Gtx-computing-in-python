# Create a list Of strings and assigns it a list of strings each with multiple words.
listOfStrings = ["This is the first string", "This is the second string",
                 "This is the third string", "This this the fourth string",
                 "This this the fifth string"]
numSpaces = 0
for currentString in listOfStrings:
    # Loops over each character in currentString
    print(currentString)
    for currentCharacter in currentString:
        if currentCharacter == " ":
            numSpaces += 1
            print(numSpaces)
print(len(listOfStrings))
numWords = numSpaces + len(listOfStrings)
print("There are", numWords, "words in these strings")
