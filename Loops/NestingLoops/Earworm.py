lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6
# Imagine you have a song stuck in your head. Worse, you have only a few lines from a song stuck in
# your head. They just keep repeating over and over. The specific lines you have stuck in your head
# are stored in the variable lyrics.
# You can only stay sane so long while doing this.Specifically, you can only listen to lines_of_sanity
# lines before going crazy. Once you've reached lines_of_sanity, your brain will finish out the current
# list, then crumble.Write some code that will print the lyrics that run through your head. It should
# keep repeating each line one-by-one until you've reached lines_of_sanity lines. Then, it should
# keep going to finish out the current verse. After that, print "MAKE IT STOP" in all caps
# (without the quotes). No break
# count = 0
# while count <= lines_of_sanity:
#
#     for i in range(0, len(lyrics)):
#         print(lyrics[i])
#         count += 1
# a = lines_of_sanity - len(lyrics)
# print(a + len(lyrics))
# for i in lyrics:
#     print(i)
"""for i in range(0, lines_of_sanity):
    count = 0
    while count <= len(lyrics):
        print(lyrics[i])
        count +=1
"""
# for i in range(0, lines_of_sanity):
#     print(lyrics[i])
"""count = 0
while count <= lines_of_sanity:
    for item in lyrics:
        print(item)
    count += 1
print("Make it stop")
"""
# print(len(lyrics)) 4


"""
count = 0
while count <= lines_of_sanity:
    # count += 1
    for i in lyrics:
        count += 1
        print(i)
        # count += 1
print("MAKE IT STOP")
"""




# a = lines_of_sanity - len(lyrics)
# print(a + len(lyrics))
# for i in lyrics:
#     print(i)
#
# count = 0
# while count <= lines_of_sanity:
#     for i in range(0, len(lyrics)):
#         print(lyrics[i])
#     count += 1
#################################################################
# Gtx Solution
# lyrics = ["I wanna be your endgame", "I wanna be your first string",
#           "I wanna be your A-Team", "I wanna be your endgame, endgame"]
# lines_of_sanity = 6

# As the hint suggested, we're going to need a counter to count how
# many lines have been played already. This is how we'll know if we've
# lost sanity yet. We'll start this at 0:

lines_heard = 0

# Now, we need two loops: a while loop while lines_heard is less than
# lines_of_sanity, and a for loop to iterate through each line of the
# song. Which one goes first?
#
# Well, we want to repeat the song while lines_heard is less than
# lines_of_sanity. Since the while loop is governing the for loop, we
# put the while loop on the outside:

# while lines_heard < lines_of_sanity:

    # Then we run a for loop for each line of the lyrics:
    # for line in lyrics:        # For each line, we want to increment out counter so we can
        # keep track of our sanity:
        # lines_heard += 1

        # Then we want to print the current line:
        # print(line)

# Then, after we're done printing the lyrics, we print MAKE IT STOP.
# Note that this is outside any of the loops because it only prints
# once, and only after the other lines are done.
# print("MAKE IT STOP")

# There are a lot of more complicated ways we could have done this,
# but this is the simplest. Note that if we wanted to cut off the
# lyrics right when lines_heard exceeds lines_of_sanity, this
# problem would actually be more complicated.
a = ["hello", "2"]
b = 2#
count = 1
while count <= b:
    for i in a:
        # print(i)
        count += 1

        print(i)