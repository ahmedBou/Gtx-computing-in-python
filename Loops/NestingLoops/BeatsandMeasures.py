beats_per_measure = 4
measures = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# In music, a song's time signature is given in terms of beats
# per measure. A common time signature is 4 beats per measure:
# for every measure of music, a conductor might count from 1
# to 4 with the tempo of the music.
#
# A song then has a number of measures. For example, a short
# song might have only 5 measures. In which case, a conductor
# would count from 1 to 4 five times. If the time signature had
# instead been 3 beats per measure, she would could from 1 to 3
# five times instead.
#
# Write a nested for loop that will print out the beats of the
# piece of music. For example, if the song had 4 beats per
# measure and only 2 measures, this would print out:
#
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
#
# We print from 1 to 4 before starting over because there are
# 4 beats per measure, and we print them all twice because there
# are two measures.


# Add your code here! Using the original values of the variables
# above, this will initially print 1 through 4 five times for a
# total of 20 lines.

for x in range(measures):
    for y in range(1, beats_per_measure+1):
        print(y)
#################################################################
# Gtx Solution
# -----------------------------------------------------------
# There are two tricky parts of this problem. We should
# generally know that we want two for loops, one inside the
# other. One will count from 1 to beats_per_measure, one will
# count from 1 to measures.
#
# Which one goes first though? Well, the inside loop runs
# several times for each run of the outer loop. So, do we want
# to go through 5 measures for each beat, or 4 beats for each
# measure?
#
# We want the latter. So, we want the beats loop _inside_ the
# measures loop.
#
# So, we start with the measures loop:

for measure in range(0, measures):

    # Above we see the second tricky part of this question.
    # If we looped from 1 to measures, we would loop one too
    # few times. So, we can start at 0, or we can start at 1
    # and go to measures + 1. Here it doesn't really matter
    # which we choose.

    for beat in range(1, beats_per_measure + 1):
        # Here, however, it does. If we want to print beat,
        # then we want it to start at 1. If we start at 1 and
        # run to beats_per_measure, though, it will run one too
        # few times. So, we go from 1 to beats_per_measure + 1.
        #
        # Then, we just print the current beat:

        print(beat)

        # We could also loop from 0 to beats_per_measure and
        # print beat + 1 instead.
