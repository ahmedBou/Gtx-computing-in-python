"""import random
numGames = int(input("How many games would you like to play?"))
# Repeats this the number of games the user chose
for i in range(0, numGames):
    print("Game start")
    # Get a random of number from 1 to 100
    hiddenNumber = random.randint(1, 100)
    # Create userGuess and give is a value that can't be correct
    userGuess = 0
    # Repeat until the guess is correct
    while userGuess != hiddenNumber:
        # Get the user's next guess as an integer
        userGuess = int(input("Guess a number: "))
        # check if the guess is too high
        if userGuess > hiddenNumber:
            print("Too high!")
        # check if the guess is too low
        elif userGuess < hiddenNumber:
            print("Too low")
        # The guess must be right!
        else:
            print("That's right!")
"""
################################################
# 2nd Solution
import random
keepPlaying = 'y'
# while keepPlaying is "y"
while keepPlaying == 'y':
    print("Game start")
    # Get a random of number from 1 to 100
    hiddenNumber = random.randint(1, 100)
    # Create userGuess and give is a value that can't be correct
    userGuess = 0
    # Repeat until the guess is correct
    while userGuess != hiddenNumber:
        # Get the user's next guess as an integer
        userGuess = int(input("Guess a number: "))
        # check if the guess is too high
        if userGuess > hiddenNumber:
            print("Too high!")
        # check if the guess is too low
        elif userGuess < hiddenNumber:
            print("Too low")
        # The guess must be right!
        else:
            print("That's right!")
    # Update keepPlaying
    keepPlaying = input("Play again (y for yes, n for no)?")

# Explanation
# So this example showed nesting two different for loops. And as an added bonus, we also nested a
# conditional inside of those two for loops.So we have three levels of control structures, an if,
# inside of a for, inside of a for. Our code is getting pretty complicated.Now, let's take what we just
# learned and apply it to our number guessing game. You can see right away that we're going to have three
# different levels of control structures,because we have three different levels of indentation.
# Here, we have a conditional, inside of a while, inside of a for.The only change we've made to our
# number guessing game is that we've started on line 2, by asking the user to input how many games they'd
# like to play.They enter a number, we convert that to an integer,and that becomes the value of our
# variable, numGames.We then run a for loop from 0 to numGames.Note that this will run the same number
# of times as running a for loop from 1 to numGames plus 1,but because we're never actually using the
# variable i anywhere in here, we don't really need to worry about its value,we just need to worry about
# whether or not this interior loop runs the right number of times.And this will cause it to run the
# right number of times.What's interesting is that, within this for loop,the interior of this code is
# identical to our earlier number guessing game.We've added a print statement on line 5,just to tell the
# user when a new game has started.But other than that, the code is identical.We still generate a new
# random number for each game.We reset the user's guess to 0 at the beginning of each game,because if
# the computer happens to generate the same random number twice in a row, we don't want the second game
# to just exit out immediately.And then we run the same while loop,as long as the user's guess is not
# the hidden number.The contents of this while loop is identical.At the end of each execution, it'll
# return to the top,
# just at that while loop, and see if the user has
# guessed the right number yet.
# If they have, it quits.
# And if they haven't, it runs again.
# It repeats, until they get the right number.
# Over here on the right, we see that the user has
# asked to play five games, and that, on the first game,
# it took them three guesses, 50, 25, and 37,
# to guess the right number.
# Their first guess was too high, so line 16 ran.
# Their second guess was too low, so line 19 ran.
# And their third guess was correct, so line 22 ran.
# After they guessed 50, for example,
# the code jumped back up to the while loop and asked,
# does the user guess equal the hidden number?
# Well, the user's guess right now is 50 after the first run,
# and the hidden number, as we can see, would end up being 37.
# That's not true, so the phrase that their user guess does not
# equal the hidden number remains true.
# And so this runs again.
# When they guess 37, though, it again
# jumps up to the while loop.
# But this time, it finds that the user guess
# does equal the hidden number.
# So this logical expression that they do not equal each other
# is no longer true, and so this code
# jumps out of the while loop.
# But what happens when it jumps out of the while loop?
# Well, there's nothing after the while loop,
# but the while loop was indented itself.
# And so if that while loop is done terminating,
# we're going to go all the way back up
# to the loop that controlled that while loop, that for loop.
# And again, it's going to ask, am I done yet?
# Well, in this case, we've run for one game,
# and yet the user asked to run for five games.
# So we're not done running every game yet.
# And so the interior of that for loop will repeat again.
# And so we repeat the entire game over again,
# this time with a new hidden number generated from scratch.
# This is getting pretty complicated,
# so let's trace through the next game.
# The game starts, and the user guesses 50.
# 50 is too high, so line 16 runs.
# 50 does not equal our hidden number,
# and so the interior of the loop runs again.
# Then the user guesses 25.
# 25 is now too low, so line 19 runs.
# 25 still doesn't equal our hidden number.
# So it's not true that the user guess equals the hidden number,
# and so the interior of the while loop runs yet again,
# and repeats for 37, for 43, for 47.
# And then, for 48, which, if this showed more, you would see
# is actually the right answer.
# Once the user guesses 48, it exits
# this while loop, returns to that for loop, asks am I done yet?
# And no, we're not, because we wanted to play five games,
# and now we've only played two.
# So it repeats again, generating another new hidden number
# and resetting the user's guess to zero once again.
# So here, we've built some pretty complicated reasoning.
# But notice that this really complicated reasoning
# that we've developed is just the exact same while
# loop that we've programmed before put inside of a
# for loop.
# We only added two actual lines of code,
# and we could have done it in one.
# And yet, adding that has dramatically
# increased the complexity of our program.
# This is actually a pretty common paradigm
# for how you design programs.
# If you're going to have something
# that you repeat a number of times, develop that part first.
# Make sure it works on its own, and then
# put it inside of a loop that will repeat it.
# If it's not going to work yet, there's
# no reason to repeat it over, and over,
# and over again, unless something about repeating
# is what makes it break.
# And finally, notice also that I put the import statement
# at the top, even though I'm not actually generating
# my random number until line 7.
# That's a common convention.
# You usually want to put any import statements that you have
# at the top of your program.
# Now, all that said, this is still
# kind of an odd design for this program.
# What if the user doesn't know how many games they
# want to play at the beginning?
# What if they think they want to play five,
# but then they decide, after three, that they're done?
# We could tweak this program and rewrite it
# with a nested while loop, instead
# of a while loop put inside of a for loop.
# Here, on line 2, instead of getting the number of games
# that the user wants to play, we create
# a variable called, keepPlaying, and give it
# the initial value, y-- y, for yes.
# On line 4, we see to run the following loop while the answer
# to keep playing is y, for yes.
# The first time line 4 runs when we first encounter the loop,
# the user hasn't had the chance to change
# the value of keepPlaying, so we're guaranteeing that this
# will be yes initially.
# Then, once again, the interior of this
# is the exact same as our original number guessing
# program-- generate the number, create the user guess,
# and keep repeating, until the user guesses the right number.
# Here though, instead of checking at the end
# to see if we've completed the right number of games,
# we end each game by asking the user to input whether they
# want to play again.
# We take that value and put it in for keepPlaying.
# Then, after that, because that's the last line
# of the outer while loop, the execution
# will return to that loop and check
# to see whether or not that logical expression is still
# true.
# If the user entered y, for yes, then keepPlaying
# will still equal yes, and so the game will run again.
# If they entered n, or in fact, if they entered anything else,
# then keepPlaying will no longer equal y.
# The loop won't repeat, and execution will terminate.
# We can see that over here in our output.
# After the first game, the user entered y, which means,
# when the execution jumped back to the outer while loop,
# it was true that keepPlaying equaled y.
# Because it was true, because that logical expression is
# true, it jumps back inside of the while loop
# and runs the game again.
# After the second game, the user entered n.
# So when execution jumped back to the while loop,
# it was false that keepPlaying equaled y,
# because now, it equals n.
# And so the loop didn't repeat, and would instead
# jump to whatever would come next in our code, which
# here, is nothing.
# And so execution ends.
# Notice especially, that we create the initial value
# of keepPlaying such that it guarantees that our loop will
# run at least once.
# That's kind of the equivalent of the
# do while loop that other languages have,
# that Python doesn't have.
# Although, we can't do a do while loop, we
# can create our initial variables,
# we can assign values to our variables
# such that it guarantees the while
# loop will run at least once.