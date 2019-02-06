for i in range(1, 6):
    j = 0
    while j < i:
        print(j, end=" ")
        j += 1
    print("")

# Note: end = " " means that print() will put a space after what was printed instead of starting
# a new line.
# What will be the output of the code above?

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0

# 2.Which of the following will have the identical output as the one above?
for i in range(1, 6):
    for j in range(0, i):
        print(j, end = " ")
    print("")
for i in range(1, 6):
    for j in range(0, i + 1):
        print(j, end = " ")
    print("")

for i in range(1, 6):
    for j in range(i, 6):
        print(j, end = " ")
    print("")

for i in range(1, 6):
    for j in range(i + 1, 6):
        print(j, end = " ")
    print("")

# Which of the following will have the identical output as the one above?

i = 0
while i < 6:
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1
    i += 1
    print("")

i = 0
while i < 6:
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1
        i += 1
    print("")

i = 1
while i < 6:
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1
    i += 1
    print("")


i = 1
while i < 6:
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1
        i += 1
      print("")
