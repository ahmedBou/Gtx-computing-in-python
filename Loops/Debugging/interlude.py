num = 5
result = 1
for i in range(num):
    print(i, result)
    result *= i
    # print(result)
print(result)

# If our result had been 1, we might assume that the problem is just that the loop isn't running at all:
# that would just mean that result was never changing. But result is changing. So, we want to know when
# it takes on the wrong value.
# I've added a print statement inside the loop. It prints both variables that are changing: i and result.
# This way, I can see exactly when the result goes off track.0 1