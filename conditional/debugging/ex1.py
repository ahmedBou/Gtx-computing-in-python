steak = False
pork = True
guacamole = True
queso = False

# Imagine you're writing code for a cash register at a
# restaurant. This restaurant serves burritoes. The base price
# of a burrito is $5. If the customer wants steak or pork, it
# adds $0.50. If they want quacamole, it adds $1.00. If they
# want queso, it adds $1.00. The customer may only select one
# meat, but they may have both queso and guacamole, neither,
# or just one.
#
# Write some code below that will print the cost of the
# burrito based on the variables above. You do not need to
# print the dollar sign or extra 0s. Remember, your final answer
# should only print out the price: comment out any debug
# statements once you have the right answer.





price = 5.00
if steak or pork:
    print("Adding 0.50 for steak or pork!")
    price += 0.50
elif guacamole:
    print("Adding 1.00 for guacamole!")
    price += 1.00
if queso:
    print("Adding 1.00 for queso!")
    price += 1.00

print(price)


"""
Uh oh. It worked when you wrote it, but now it's not passing the autograder. Why not? Let's look at how
to interpret the results.

The output on the right says:

We tested your code with steak = False, guacamole = True, pork = True, queso = False. We expected your
code to print this: 
6.5

However, it printed this:
5.5

Notice the variable values: when we wrote our code, guacamole was False. The autograder is testing it
when guacamole is True. The expected answer here makes sense, though: pork adds 0.5, guacamole adds 1.0,
and so the answer really should be 6.5. So, it appears our code only worked correctly when guacamole was
False. We have to test it with different inputs to see if it really works!

1.Debugging
So how do we fix this problem? There are two things we should generally do.
First, let's change the values in our code to reflect the test case that our code is failing! That way,
we can debug in more detail. Our code failed the test case where guacamole was True (and nothing else was
different), so let's change guacamole to True.
Second, we want to know what is currently happening with the code. To do that, we want to trace through
it, which we can do by adding some debug statements. We want to print inside each branch of the code so 
that we can see which branch or branches are running, then run the code:
 */*Based on that output, which of the following lines are being executed? line26 and 27
 */*Based on the directions and the current values of the variables, which of the following lines should
have been executed?line 26 , 27,29,30
*/*Which of the following best describes the error in the code that is breaking this test case? 
(There may be other errors, but they are not the cause of this test case behaving incorrectly.):
The elif on line 28 means guacamole is never selected if steak or pork was True. Because of that elif,
the code skips right over guacamole if steak or pork was True.

2. Revising the Code
Notice how those debug statements have helped us narrow down what's going wrong: lines 29 and 30 aren't
running when they should. We also see that lines 26 and 27 are running, which helps us see that the elif
prevents lines 29 and 30 from running.
Now, based on these debug statements, finish fixing the code below. Note that there may be other problems
besides the ones we explored here.
Generally (at least until you get to much more advanced projects), you'll want to comment out these debug
statements when you're done because they aren't intended to be part of the finished product. The same 
applies here: this autograder won't accept your answer if the debug statements are still printed, so just
comment them out when you're done!
"""