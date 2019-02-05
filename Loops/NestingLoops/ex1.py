count = 0
for x in range(3):
    for y in range(3):
        count += y
print(count)
# Correct: Right! When you trace through this code, it basically adds 0 + 1 + 2 + 0 + 1 + 2 + 0 + 1 + 2.
count = 0
for x in range(3):
    for y in range(3):
        count += x
print(count)
# Correct: Right! When you trace through this code, it basically adds 0 + 0 + 0 + 1 + 1 + 1 + 2 + 2 + 2.
count = 0
for x in range(3):
    for x in range(3):
        count += x
print(count)
# Right! When you trace through this code, it basically adds 0 + 0 + 0 + 1 + 1 + 1 + 2 + 2 + 2.
# It doesn't matter that we're using x as the variable for both loops.