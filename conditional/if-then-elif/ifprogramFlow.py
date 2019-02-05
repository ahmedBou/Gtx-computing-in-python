# name = input("Please enter your name:")
# age = int(input(f"How old are you, {name} ? "))
#
# if age >= 18:
#     print("you are old enough to vote")
#     print("please put an x in the box")
# else:
#     # print("you must wait {} years".format(18-age))
#     print(f"you must wait {18-age} years")
print("Please guess a number between 1 and 10: ")
guess = int(input("enter your guess number"))
# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done you guessed it ")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > 5:
#     print("guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done you guessed it ")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time ")
# 2. Great solution
if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else: # guess must be greater than 5
        print("Please guess lower")
    guess = int(input()) # this line will be executed no matter what because we haven't
    # got any tests, and it's not intended to the next level
    if guess == 5:
        print("Well done, You guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")