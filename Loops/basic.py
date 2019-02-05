# In the designated areas below, write the three for loops
# that are described. Do not change the print statements that
# are currently there.
print("First loop:")
for i in range(1, 11):
    print(i)

# Write a loop here that prints the numbers from 1 to 10,
# inclusive (meaning that it prints both 1 and 10, and all
# the numbers in between). Print each number on a separate line.
print("Second loop:")
for i in range(-5, 6):
    print(i)
# Write a loop here that prints the numbers from -5 to 5,
# inclusive. Print each number on a separate line.

print("Third loop:")
for i in range(1, 21):
    if i % 2 == 0:
        print("Third loop:", i)

# Write a loop here that prints the even numbers only from 1
# to 20, inclusive. Print each number on a separate line.
# Hint: There are two ways to do this. You can use the syntax
# for the range() function shown in the multiple-choice
# problem above, or you can use a conditional with a modulus
# operator to determine whether or not to print.
#############################################################
# Gtx solution
#The first two of these loops are relatively
#straightforward. We have a first item, a last item, and
#we're printing every item in between.

print("First loop:")

#This loop should print 1 to 10. Remember, the range()
#function includes the first argument but excludes the
#second argument. So, we have to make the second argument
#one larger than where we want to end:

for i in range(1, 11):
    print(i)


print("Second loop:")

#This loop should print from -5 to 5. Really, it's the
#same as the previous one, but the start and end points
#are different. So, we just change the arguments to
#range():

for i in range(-5, 6):
    print(i)


print("Third loop:")

#This third one is tricky, though. We want to print the
#even numbers only. We can do that two ways.

#One, we can use the syntax shown in the multiple choice
#exercise before this problem:

for i in range(2, 21, 2):
    print(i)

#Notice that we've put three numbers into the range()
#function. The first one is our start number and the
#second is our end number as usual. The third, though,
#is the 'step' number. That means how many numbers
#should we advance each time the loop runs. By setting
#it to 2, we advance two numbers each time the loop
#runs: 2, 4, 6, 8, etc. We could also make this
#negative to run the loop backwards!

#The other way, though, is to check to see if each
#number in a more typical range is even, and only print
#it if it is:

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#This loop goes through all the numbers 1 through 21,
#but the print statement is under a conditional, and
#the conditional checks if the number is even. So, it
#only prints if the nubmer is even.