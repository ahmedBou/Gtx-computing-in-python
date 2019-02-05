import random
# Get a random number from 1 to 100
hiddenNumber = random.randint(1, 100)
print(hiddenNumber)
# Create userGuess and give is a value that can't be correct
userGuess = 0
while userGuess != hiddenNumber:
    # Get the user's next guess as an integer
    userGuess = int(input("Guess a number: "))
    # Check if the guess is too high
    if userGuess > hiddenNumber:
        print("Too High")
    # check if the guess is too low
    elif userGuess < hiddenNumber:
        print("Too low")
    # the guess must be right
    else:
        print("that's right!")

