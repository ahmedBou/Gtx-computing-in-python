mystery_string = "Hello! What a fine day it is today."
mystery_character = "a"

# -----------------------------------------------------------

# Write some code below that will count and print how many
# times mystery_character appears in mystery_string. You may
# not use the string class's .count method.
#
# With the original values for mystery_string and
# mystery_character, your code should initially print 4. Only
# count characters with the same case as mystery_character
# (in other words, here you would ignore capital A).
# print(mystery_string[1])
count = 0
for currentString in mystery_string:
    # print(currentString)
    if currentString == mystery_character:
        count += 1
    # for currentCharacter in currentString:
        # print(currentCharacter)
        # if currentCharacter == mystery_character:
        #     count += 1
print(count)

#########################################################
# Gtx Solution
# First, we're counting something, so we start by initializing
# a counter to 0:
count = 0

# Now, we want to iterate through each character in mystery_string.
# We can do that with this loop:
for a_character in mystery_string:

    # Next, we want to compare the current character in the string
    # to mystery_character to see if they're the same.
    if a_character == mystery_character:
        # If so, we add to the counter:
        count += 1

# Then, at the end, we print the counter:
print(count)
