mystery_int = 50

# Add some code below that will find and print the sum of
# every odd number between 0 and mystery_int. This time,
# exclude the bounds (e.g. if mystery_int was 51, add the odds
# from 1 to 49, but not 51).
#
# Hint: There are multiple ways to do this!
sum = 0
for i in range(1, mystery_int):
    if i % 2 != 0:

        sum += i
print(sum)
###########################################################
# Gtx Solution
#-----------------------------------------------------------
# Like the previous problem, there are two ways we could do
# this: one with the step argument, one with the modulus
# operator.
#
# Either way, though, we need to initialize a variable to
# hold our sum, add to our sum when appropriate, and print
# our sum at the end.
#
# Here's the solution using the step argument:

current_sum = 0
for i in range(1, mystery_int, 2):
    current_sum += i
print(current_sum)


# Here's the solution using the modulus operator:

current_sum = 0
for i in range(1, mystery_int):
    if i % 2 == 1:
        current_sum += i
print(current_sum)

# Notice that because we want to sum the numbers from 1 to
# mystery_int *excluding* mystery_int itself, both our
# loops run to mystery_int instead of mystery_int + 1.