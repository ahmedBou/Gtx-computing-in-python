mystery_int = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# In math, factorial is a mathematical operation where an
# integer is multipled by every number between itself and 1.
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1, or 120.
# Factorial is represented by an exclamation point: 5!

# Use a for loop to calculate the factorial of the number
# given by mystery_int above. Then, print the result.
#
# Hint: Running a loop from 1 to mystery_int will give you
# all the integers you need to multiply together. You'll need
# to track the total product using a variable declared before
# starting the loop, though!
factor = 1
#a = int(input("enter the number"))
for i in range(mystery_int, 1, -1):
    print(factor)
    print(i)
    print(f"{factor}= {factor}*{i}")
    factor *= i
print(factor)

# 1st Gtx Solution
#To do this, we're going to use a common programming pattern:
#we're going to have a variable created before the loop that
#gets updated by the loop. Here, that variable is going to
#hold the product of all the numbers between 1 and
#mystery_int, so let's call it product.
#
#What value should we give product initially? We have a
#couple options:
#
# - We could initially assign it to 1. That way, whatever
#   it's multiplied by first will be its new value.
# - We could assign it to mystery_int. Then, if we run
#   the loop to multiply the product by all the numbers
#   before mystery_int, then mystery_int's value is in the
#   product, too.
#
#Let's do the first one.

product = 1

#...then we want to loop from 1 to mystery_int, multiplying
#product by each number:

for i in range(1, mystery_int + 1):
    product *= i

#Notice a couple things:
#
# - We could have started the loop at 2. Multiplying by 1
#   doesn't change the value.
# - Although we usually show factorial as being calculated
#   in descending order (5 * 4 * 3 * 2 * 1), multiplication
#   is transitive, so it's fine that our loop actually
#   calculates 1 * 2 * 3 * 4 * 5.
# - We run the loop until mystery_int + 1. That's because
#   range is exclusive: the second number given to range
#   isn't part of the list of numbers it uses. So, we add
#   one to mystery_int to have it incorporate that last
#   number.
# - The first time the loop runs, its value is 1, and it's
#   multiplied by 1. So, its value is 1. The second time,
#   its value is 1, and it's multiplied by 2, so its value
#   is now 2. The third time, its value is 2 (because it
#   was changed by the previous iteration of the loop), and
#   it's multiplied by 3, so its value is now 6 -- and so
#   on until it reaches mystery_int.
#
#Now finally, we print the final product:

print(product)

#Notice that this line is not indented. If it were indented,
#it would print several times -- one for each iteration of
#the loop. We only want it to print once at the end, so we
#do not indent it: that way, it is not controlled by the
#loop.
#
#Remember, Python ignores these comments. As far as Python
#is concerned, the code in this file is identical to the
#code in sample_answer_2.py. The alternate approach is also
# shown in sample_answer_3.py.
# 2nd Gtx solution:
#Here is an alternate approach, provided just for reference:

mystery_int = 5
product = mystery_int
for i in range(1, mystery_int):
    product *= i
print(product)