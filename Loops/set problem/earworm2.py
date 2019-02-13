lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6


# Recall the Ear worm problem (3.3.5 Coding Exercise 2). The
# first time, you would still finish printing the entire list
# of lyrics after lines_of_sanity was exceeded.
#
# Revise that code so that you always stop when lines_of_sanity
# is reached. If lines_of_sanity is 6, you would print 6 lines,
# no matter how many lines are in the list. If there are fewer
# than 6 lines in the list, then you'd repeat the list until
# the number of lines is reached.
#
# For example, with the values above, you'd print:
# I wanna be your endgame
# I wanna be your first string
# I wanna be your A-Team
# I wanna be your endgame, endgame
# I wanna be your endgame
# I wanna be your first string
# MAKE IT STOP
#
# That's 6 lines: the entire list once, then the first two lines
# again to reach 6. As before, print MAKE IT STOP when you're
# done.
#
# HINT: There are multiple ways to do this: some involve a small
# change to our earlier answer, others involve a more wholesale
# rewrite. If you're stuck on one, try to think of a totally
# different way!


# Add your code here! Using the initial inputs from above, this
# should print 7 lines: all 4 lines of the list, then the first
# two lines again, then MAKE IT STOP
count = 0
while count < lines_of_sanity:
    for i in lyrics:
        count += 1
        if count > lines_of_sanity:
            break
        print(i)
print("Make it stop")

########################################################################
# GTx Solution :
# There are a lot of ways to do this, but many of them rely on things
# we haven't learned yet. So, first, let's do this using only what we've
# covered so far.
#
# We're still going to need to count the number of lines heard so far:
lines_heard = 0

# And we're still going to want to repeat until lines_heard exceeds
# lines_of_sanity:
while lines_heard < lines_of_sanity:

    # And we still want to iterate over each line in the lyrics:
    for line in lyrics:

        # The difference here is: we only want to print if lines_head
        # still doesn't exceed lines_of_sanity. It's possible that it
        # exceeded it since the last time the while loop condition was
        # checked since it could be incremented several times inside
        # this for loop.
        #
        # So, we only want to print if it's still less:

        if lines_heard < lines_of_sanity:
            lines_heard += 1
            print(line)

        # Technically, we could break here: it would stop the for loop,
        # send us back to check the while loop, and that would
        # terminate. We don't really need to, though. Without that, the
        # for loop will run a few more times, but they still won't print
        # anything.

print("MAKE IT STOP")

# There's a more elegant way to do this, though. Check out
# sample_answer_2.py to see how.
######################################################################
# 2nd GTx Solution:
# The more elegant solution relies on being able to access individual
# elements from lyrics by number. We'll cover how to do that in chapter
# 4.3. However, here's what that will look like:
#
# First, we're just going to use lines_of_sanity as our range for our
# for loop. After all, we know exactly how many lines we need to print.

for i in range(0, lines_of_sanity):
    # Next, we want to print a line from lyrics. Which line? Well, for
    # the first four lines, we want to print the line at the index of
    # i.
    #
    # After that, though, i might exceed the length of the list. What
    # do we do then? Well, instead of just printing the item at
    # index i, we want to print the item at index i % length. That way,
    # if i is greater than the length, it 'wraps around' to the start
    # again.
    #
    # So, that would look like this:

    print(lyrics[i % len(lyrics)])

    # The brackets after parentheses let us specify which item in lyrics
    # we're printing. i % len(lyrics) finds which lyric to print right
    # now. If i is 4 and there are 4 lyrics, then it will print the first
    # one again. if i is 6 and there are 4 lyrics, it will print the
    # third one again.

print("MAKE IT STOP")
