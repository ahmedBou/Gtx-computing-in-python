# Runs this loop 20 times
for i in range(1, 21):
    # checks if i is even
    if i % 2 == 0:
        # Skips the rest of the code block if so
        continue
    # Prints that i is odd
    print(i, "is odd.")
print("Done")
# There are three final key words with loops that are worth
# covering, although to be honest I find relatively
# few opportunities to use these.
# They're covered here in part for the sake of completeness,
# and part so that you can recognize them
# if you come across them, and part just in case
# you ever need them.
# But don't be surprised if you don't see these
# very often in the wild.
# These three key words are all similar in that each of them
# will be the only thing that appears
# on the line on which it's placed.
# So whereas we always follow the key word
# for with a variable name, continue, pass, and break
# always exist on their own line.
# The continue statement or the continue
# keyword forces the current iteration of the loop to stop,
# skipping over any remaining code inside the loop.
# So in this code, we're running a loop from 1 to 20.
# And during each iteration of the loop,
# we check to see if the number of the current iteration is even.
# Remember, i modulus 2, or i % 2, will return of the remainder
# of the value of i divided by 2.
# If i is even or the value of i is even,
# then the remainder will be 0.
# If the value is odd, then the remainder will be one.
# Here we only want to print if i is odd.
# We know this range function will create
# a list of numbers 1 through 20, and the body of this loop
# will run once for every number in that list.
# So when i is one, its faults-- that i % 2- is zero.
# So line 6 is skipped, and line 8 runs printing.
# Sure enough-- 1 is odd.
# Then, when i is 2, it's now true that i % 2 equals 0.
# The remainder of 2 divided by 2 is zero.
# And so line 6 will run.
# Line 6 just says continue.
# Continue says-- skip the remainder of this iteration
# of this loop and go ahead and jump back to the loop
# and check to see if we're done yet.
# So because execution encountered continue
# before it hit line 7 and 8, it just
# skips line 7 and 8 altogether.
# Note that that's kind of interesting.
# Line 7 and 8 weren't inside any kind of control structure
# corresponding to that if.
# They're inside that for, but the key word
# continue forces Python to go back and check the loop,
# skipping any remaining code in the current iteration.
# If this for loop was actually nested-- if it was inside
# of another for loop-- continue will correspond
# to the closest for loop.
# So it would terminate the current iteration
# of the inner loop, not the outer loop.
# Our second keyword is break.
# Like continue, break skips the rest of the current iteration
# of the loop.
# But instead of skipping back to the actual loop
# itself and checking to see if we're done yet,
# break forces execution to skip to the next line of code
# after this loop.
# So as before, this loop is going to run from one to 20.
# When i is 2, it's false that i mod 2 is 0,
# so line 6 will be skipped.
# Line 8 will run and print that 1 is odd.
# Then, on the second run, i had the value 2.
# 2 & 2, or 2 mod 2, is 0, and so line 6 runs.
# Line 6 not only skips the remainder
# of the current iteration, but it doesn't even
# bother checking to see if the loop was done running.
# It forces execution to break out of the loop
# and jumps straight to the next line of code after the loop.
# So here, line 7 and 8 are skipped, as well as the rest
# of the numbers in that range.
# And we go ahead and print none.
# And, finally, the third advanced loop keyword we might use
# is called pass.
# I don't have an example for it here.
# Pass exists because, remember, every time we
# use a control structure, the next line of code
# must be indented.
# But there will be certain rare times when
# we need to use a control structure,
# but we don't want to do anything inside of it.
# One example might be-- imagine we
# know we're going to want to loop somewhere,
# but we haven't implemented its contents yet.
# We want to leave the loop there for now,
# but we don't want to bother with the interior of it.
# We could use pass just to skip over
# the inside of that loop for now until we come back
# to implement it.
# So, effectively, pass is just like Python's way of leaving
# a blank indented line.
