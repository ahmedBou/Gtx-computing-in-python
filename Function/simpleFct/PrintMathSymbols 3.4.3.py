# When writing out mathematical equations for younger
# audiences, we usually want to use the traditional division
# and multiplication symbols, ÷ and ×, instead of slashes and
# asterisks. These keys aren't on the keyboard, though. So,
# let's write functions that will print them.
#
# First, write two functions: one called print_division_symbol
# and one called print_multiplication_symbol. The functions
# should do what their names suggest: print_division_symbol
# should print a division symbol, print_multiplication_symbol
# should print a multiplication symbol. You can copy the
# characters for those symbols from these directions.
#
# Then, after writing those two functions, call them in the
# same order: print_division_symbol, then
# print_multiplication_symbol. The output of your code should
# thus be ÷, then ×, each on their own line.
#
# Note that you don't need to worry about the end="" thing
# you saw in the video: just print the symbols on their own
# lines. Note also that if you receive a UnicodeEncodeError,
# try submitting your code instead of running it: that error
# happens sometimes, but only affects Run, not Submit.
#
# HINT: you're writing two functions. You don't want one to
# be inside the other.


#Write your two functions here!

def print_division_symbol():
    print("÷")


def print_multiplication_symbol():
    print("×")


#Call your two functions here!

print_division_symbol()
print_multiplication_symbol()

# Gtx Solution
# -----------------------------------------------------------
# To start, we know we need a functions called
# print_division_symbol and print_multiplication_symbol. Let's
# start with multiplication.
#
# To create a function called print_multiplication_symbol, we
# first enter this:

def print_multiplication_symbol():
    # As with all functions, it starts with the keyword 'def',
    # followed by the function name, then an open parenthesis.
    # If there were arguments, we would list them inside the
    # parentheses, but since there are not, we just close it.
    # Then, we end with a colon, just like with any other
    # control structure.
    #
    # Now we're inside the function, so we add the line of
    # code that does what we need the function to do:

    print("×", end="")

    # Now we're done, so nothing after this should be indented.
    # If we indent whatever comes next, it will still be inside
    # this function.


# Next, we'll do the same for division:
def print_division_symbol():
    print("÷", end="")


# Now, notice that we declared those functions in the opposite
# order of the directions, but it doesn't matter. We can
# declare them in whatever order we want as long as we call
# them in the correct order:
print_division_symbol()
print_multiplication_symbol()

# Because we call print_division_symbol() first, the division
# symbol is printed first, even though the function for
# multiplication is declared first.
