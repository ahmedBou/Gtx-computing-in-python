mystery_int = 7
for i in range(1, mystery_int+1, 3):
    print(i)
# for i in range(1, mystery_int):
#     if i % 3 == 0:
#         print(i)

# Gtx Solution
# There are at least two ways we could do this. The first
# uses an extra argument for range():

for i in range(1, mystery_int + 1, 3):
    print(i)

# By adding 3 as our third argument (called the 'step'), we
# tell Python to give us every 3rd number starting at 1.
# Note that we have to run to mystery_int + 1 because the
# range function runs up to, but does not include, the
# second argument. If we exclude the + 1, then we wouldn't
# get the last number in some cases.

# The other approach is to use the modulus function: iterate
# over every number, but only print if dividing it by 3
# gives a remainder of 1. That's what's in common between
# the numbers 1, 4, 7, 10, etc.:

for i in range(1, mystery_int + 1):
    if i % 3 == 1:
        print(i)