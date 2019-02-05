myString = "There are seven words in this string."
numSpaces = 0

# Runs this loop for each character in the string
for currentCharacter in myString:
    # Checks if the character is a space
    if currentCharacter == " ":
        numSpaces += 1
print("There are " + str(numSpaces + 1) + " words in the string.")
# numSpace + 1 because the last word in the string won't end in a space