# Here is some code for a for loop
j = 0
for i in range(0, 10):
    print(j, "more and we're done!")
    j = -1
print("We're done!")

# This code prints 10 lines of output, from "10 more times!" to "1 more times!". Then it prints,
# "We're done!".

# We noted earlier that every for loop can be rewritten as a while loop. Here's our attempt to rewrite' \
#  this loop as a while loop:
j = 10
while j > 0:
    j -= 1
    print(j, "more times!")
print("We're done!")
# However,the output of this while loop is different from the output of the for loop.How is it different?
# Try to answer without running the code!
# answer :Its print statements are one too low: it prints from "9 more times!" to "0 more times!" instead
# of "10..." to "1...".
# Which of the following changes could fix this code:
# Move line 4 above line 3.
# That's right! The issue is that the loop runs the right number of times, but we're subtracting 1
# from j before printing it. So, all the numbers are off-by-one. By printing before subtracting,
# we achieve the same output as we had originally.
# That also mimics the behavior of the for loop: it only increments the variable at the end of the loop.