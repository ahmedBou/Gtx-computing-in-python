# We've written the function, reverse, below. This function
# takes a string and returns the reverse of it. There are two
# scope errors somewhere in the code. Read through all the
# code below to find and fix the errors, so that the function
# produces the correct output and the result of the function
# is correctly printed. Note that you should not change the
# three lines that are already present in the function, but
# you may add lines before them, or you may change or add to
# the lines outside the function.
#
# Note that your goal here is to fix both the function itself
# and the program as a whole. So, your function should be
# able to be called on a new string, and the program when
# run should print the reverse of the string originally on
# line 29.


def reverse(a_string):
    # You may add code before the following three lines.
    rev = ''
    # Don't change these three lines.
    for i in range(len(a_string) - 1, -1, -1):
        rev = rev + a_string[i]
    return rev


# You may change or add to the following lines.
rev_R = reverse("This string should be reversed!")
print(rev_R)

##############################################################
# GTx Solution:
# If you run the original code, the first error you encounter
# is inside the function, on the line rev = rev + a_string[i].
# The error is that the variable rev is being used on the
# right side of the expression before it's actually given
# a value. The first time that line is called, it adds
# a_string[i] to the current value of rev, but rev has no
# current value.
#
# So, we first need to create rev with an empty string so that
# it exists when we need it. So, we add that before the
# current code inside the function:

def reverse(a_string):
    # You may add code before the following three lines.

    rev = ""  # THIS LINE IS NEW!

    # Don't change these three lines.
    for i in range(len(a_string) - 1, -1, -1):
        rev = rev + a_string[i]
    return rev


# After making that change, though, there is still a problem
# on the lines below. The error is the same. The last line
# tries to print rev when rev does not have a value. But
# wait: didn't we give rev a value inside the function
# reverse()? And aren't we calling reverse() before trying
# to print rev?
#
# Remember, the variable rev is created inside the function
# reverse(). That means it only exists inside that function.
# When the function is over, it ceases to exist, unless it's
# returned: and if it's returned, we need to capture the
# result. So, that's what we need to do: modify the first
# line below to capture the result.

rev = reverse("This string should be reversed!")
print(rev)

# Now when rev is returned on line 21, the right side of
# line 37 is replaced by that value. So, the variable rev
# created on line 37 (a different variable with the same
# name as the one inside the function) receives that value,
# and we can print it on line 38.

