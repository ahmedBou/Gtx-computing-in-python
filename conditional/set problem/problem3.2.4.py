cafe = "Galloway"
balance = 5

# You may modify the lines of code above, but don't move them!
#  When you Submit your code, we'll change these lines to
#  assign different values to the variables.
#
#  Atlanta is full of great coffee places. Unfortunately, great
#  coffee is usually expensive. The variables above will
#  contain a balance and a cafe name. Below are the prices of
#  a cup of coffee at each of three locations:
#
#  - Octane: $6
#  - Galloway: $5
#  - Starbucks: $4
#  - Revelator: $3
#  - Dunkin: $2
#
#  Add some code above that will print one of the following
#  two messages depending on whether the value of balance is
#  high enough to buy a cup of coffee at the given cafe.
#
#  - If it is sufficient, print "With [balance] dollars, I
#    can buy coffee at [cafe]"
#  - If it is not sufficient, print "With [balance] dollars,
#    I cannot buy coffee at [cafe]"
# Octane = 6
# Galloway = 5

"""
if cafe == "Octane" or balance >= Octane:
    print("With {} dollars, can buy coffee at {}".format(balance, cafe))
#elif cafe == "Galloway" and balance >= Galloway:
#    print("With {} dollars, can buy coffee at {}".format(balance, cafe))
else:
    print("With {} dollars, I cannot buy coffee at {}".format(balance, cafe))
"""
if cafe == "Octane" and balance >= 6:
    print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
elif cafe == "Galloway" and balance >= 5:
    print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
elif cafe == "Starbucks" and balance >= 4:
    print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
elif cafe == "Revelator" and balance >= 3:
    print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
elif cafe == "Dunkin" and balance >= 2:
    print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
else:
    print("With {} dollars, I cannot buy coffee at {}".format(balance, cafe))
# 1st Gtx Solution
cafe = "Octane"
balance = 7.5

# -----------------------------------------------------------
# It's tempting to check each possible combination of cafe
# and cost separately, and print inside the conditional.
# Remember, though, that we want to limit duplicated code.
# If we see the same line of code lots of times, we probably
# want to redesign (called 'refactoring' with code) it to
# only use that line once.
#
# Here's one possible way to do this without putting a print
# statement in each branch of the conditional. First, we
# assume that we can afford it unless we find evidence that
# we cannot:

can_afford = True

# Then, for each possible cafe, we check if we can't afford
# it. If we can't, we change can_afford to False:

if cafe == "Octane" and balance < 6:
    can_afford = False

# Notice here that we're using an additional 'if' instead of
# an elif. The reason is that if the conditional above wasn't
# True because it was the wrong cafe, then we still want to
# check the other cafes.

if cafe == "Galloway" and balance < 5:
    can_afford = False
if cafe == "Starbucks" and balance < 4:
    can_afford = False

# Notice also that we could revise this to use a bunch of 'or'
# operators, but that would lead to a loooong line of code.
# We'd rather avoid that.
if cafe == "Revelator" and balance < 3:
    can_afford = False
if cafe == "Dunkin" and balance < 2:
    can_afford = False

# Now, can_afford holds whether we can afford it or not, so
# we can just print our message depending on its value:
if can_afford:
    print("With", balance, "dollars, I can buy coffee at", cafe)
else:
    print("With", balance, "dollars, I cannot buy coffee at", cafe)

# Now, there is a clever, weird way to do this as well. Check out
# sample_answer_2.py to see it.
###################################################################
# 2d Gtx Solution:
cafe = "Octane"
balance = 7.5

# -----------------------------------------------------------
# Notice that the two possible messages we might print are
# only different by three characters: we either print 'can'
# or 'cannot'. So, why not instead make that the variable we
# change?
#
# Most of our code is the same, but notice that we've changed
# can_afford to a string instead of a boolean:

can_afford = "can"

# Our code is the same, but we change can_afford to "cannot"
# if we can't afford the coffee instead of changing it to False.

if cafe == "Octane" and balance < 6:
    can_afford = "cannot"
if cafe == "Galloway" and balance < 5:
    can_afford = "cannot"
if cafe == "Starbucks" and balance < 4:
    can_afford = "cannot"
if cafe == "Revelator" and balance < 3:
    can_afford = "cannot"
if cafe == "Dunkin" and balance < 2:
    can_afford = "cannot"

# The benefit to this is that we don't need a final conditional at
# the end of our program. Instead, we just print the final value
# of the variable can_afford:

print("With", balance, "dollars, I", can_afford, "buy coffee at", cafe)

# If we could afford it, can_afford is the string "can". If we couldn't,
# can_afford is the string "cannot". Either way, the message ends up
# correct!
