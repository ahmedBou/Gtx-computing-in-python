mystery_string = "CS1301"

# Write a for-each loop that lists each character in
# mystery_string with its index. For example, if the string
# was "David", the output would be:
# 0 D
# 1 a
# 2 v
# 3 i
# 4 d
#
# Note that the first item is #0, the second is #1, and so
# on! We'll talk about why that is in Unit 4.
#
# Hint: You'll need a separate variable to keep track of how
# many letters you've printed! You may not use the range
# function on this problem.
print(mystery_string[1])
char = 0
# char = -1
for i in mystery_string:
    # char += 1
    print(char, " ", i)
    char += 1
"""
for i in range(0, len(mystery_string)):


    print( i," ",mystery_string[i])
"""
# The Gtx solution
# -----------------------------------------------------------
# As we get into more complex problems, we might find that
# we don't always write our programs in order. We might build
# them from the inside out. Let's walk through this one that
# way. We'll comment out the code as we build it, then supply
# the final code at the end.
#
# So, we know we want to iterate over each letter in the
# string. The videos above showed us how to do that:

# for letter in mystery_string:

# That for-each loop will go through each letter one-by-one,
# assigning it to the variable letter. What else do we want
# to do? Well, we want to print each letter, too:

# for letter in mystery_string:
#     print(letter)

# That will print each letter on its own line. However,
# that's not all we wanted to do. We also wanted to print
# the numbers for each letter in the string. How do we do
# that?
#
# If we were using range, we'd have each number in order,
# but we're not. So, we need to track that separately!
# So, before the loop starts, we create a variable that
# will hold how many characters in the string we've looked
# at:

# count = 0
# for letter in mystery_string:
#     print(letter)

# Then, we also need to add 1 to it every time we print a
# letter from the string:

# count = 0
# for letter in mystery_string:
#     print(letter)
#     count += 1

# Finally, we need to change what we're printing so that
# we print the number as well. Then, we're done!

count = 0
for letter in mystery_string:
    # print(count, letter)
    print(f"the{count} is {letter}")
    count += 1
