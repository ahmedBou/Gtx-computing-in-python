# Get the number of numbers to average
numCount = int(input("How many numbers would you like to average? "))
# Loop numCount times
sum = 0
for i in range(1, numCount+1):
    # Create sum with the value 0
    # sum = 0
    # Gets the user's number
    nextNumber = int(input("Enter number #" + str(i) + ": "))
    # Add the inputted number to the sum
    sum += nextNumber
# Print the sum over numCount
print(sum / numCount)

# Finally, we should briefly talk about scope
# in the context of loops.
# As we said with conditionals, the scope of a variable
# is the area of the program's execution
# where the variable can be seen.
# In Python, a variable scope is effectively anything
# after the variable is created.
# It doesn't matter if it's declared inside a loop
# or inside a conditional or outside the loop.
# Anything after the variable is created
# is within the variable's scope.
# Now with conditionals, this presents a challenge
# if a variable was created inside a conditional then referred
# to outside the conditional.
# If the conditional didn't run-- which by design sometimes it
# wouldn't-- then the variable was not created.
# And referring to it later would create an error.
# This isn't as big a deal in loops though.
# We rarely create loops that might not run at all.
# It can happen, but it isn't a common decision
# in my experience.
# However, loops create a different issue
# for creating variables inside loops.
# The first time you assign a value to a variable Python
# creates the variable.
# Here the variable sum doesn't exist
# until we set it equal to zero.
# But the second time it encounters an assignment
# operator acting on a variable it just
# changes the variables value.
# So sum equals zero works for creating the variable sum
# and giving its initial value of zero
# and also works for updating or resetting the value of sum.
# That means that if you create a variable inside the loop,
# then every time the loop runs its value is replaced.
# Now, many times it's perfectly fine.
# For example, in our number guessing game,
# we had one variable-- user guess--
# and its value was updated every time
# the user guessed a new number.
# We both created it and assigned it inside the loop.
# And that was perfectly fine because we never
# needed it outside the loop.
# However, if you're going to reference the variable outside
# of the loop-- as we're doing here--
# then you're going to encounter a problem.
# The code will still run just fine.
# It just won't do what we expect, unless we were just
# looking for the last value after a loop ran or something.
# Here, for example, we're trying to average the numbers
# that the user input.
# And yet every time this loop runs that gets the next number,
# sum is reset to 0.
# So when the loop runs the first time, sum is set to 0.
# Next number becomes 91 because that's what the user inputted.
# And then sum is set equal to itself plus 91.
# And so right now the value of sum is 91.
# When the next run of the loop starts,
# execution then returns, finds that the user hasn't inputted
# in all the numbers they want to input yet, and so the loop
# runs again.
# But the first thing that happens when the loop runs again
# is that sum is reset to 0.
# Then, the user enters 92, and sum is set to itself plus 92.
# But, remember, sum was just reset to 0.
# So, now, sum equals zero plus 92.
# Now, sum just equals 92.
# Every time this loop runs sum is first reset to the value 0.
# So when we get to the end, our sum
# is just the last value entered.
# In this case, that was 95, and 95 divided by 5
# equals 19-- when we can tell that the answer should be 93.
# We can avoid this by creating any variables
# that we're going to refer to after the loop
# outside of the loop.
# So here we create sum on line 2, and then we run our loop.
# That means that sum's value isn't
# reset every time the loop runs.
# Instead, we're just adding to it or updating it.
# And so when we reach the end, sum correctly
# equals 465, which divided by 5 equals 93.
# So my general advice-- if you're going
# to need to use a variable after a loop,
# then don't define it inside the loop.