mystery_value = 87


# Write a while loop that continues to add 9 to mystery_value
# until mystery_value is greater than 100. Each time 9 is
# added, print the *new* value of mystery_value. For example,
# with mystery_value = 87, your code should print 96 and 105.
while mystery_value <= 100:
    # print(mystery_value)
    mystery_value += 9
    print(mystery_value)
#################################################################
# Gtx's Solution
# -----------------------------------------------------------
# The directions state to repeat something until mystery_value
# is greater than 100. In other words, we want to repeat that
# action while mystery_value is not greater than 100. We could
# write this in two ways:

# while mystery_value <= 100:
# while not mystery_value > 100:

# Because we want to loop until mystery_value is *greater*
# than 100, we would run our while loop while it's less than
# *or equal to* 100. For that reason, it might be more logical
# to use the latter option since it's a more direct
# illustration of what the directions are asking for.

while not mystery_value > 100:
    # Then, what do we do in the loop? The directions said to
    # add nine and print the *new* value of mystery_vaule. So,
    # first we add, then we print:

    mystery_value += 9
    print(mystery_value)

# And that's all! There's nothing we needed to do after the
# loop is done.
#
# Notice that if mystery_value was greater than 100 to begin
# with, the loop will never do anything.