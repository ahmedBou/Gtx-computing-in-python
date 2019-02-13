mystery_int = 46

# Use a while loop to create a countdown from mystery_int to
# 0. Count down by 3s: if mystery_int is 46, then you should
# print 46, 43, 40, etc. Do not print any number lower than 0.
# Note that you should print both the original value of
# mystery_int and 0 if you land on it exactly.
while mystery_int >= 0:
    print(mystery_int)
    mystery_int -= 3
    #print(mystery_int)

# Gtx Solution
# We've done similar problems before, but this one has a
# small twist: we want to print the number before it's
# changed, not after:

while mystery_int >= 0:
    print(mystery_int)
    mystery_int -= 3