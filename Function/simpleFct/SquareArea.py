# Write a function that takes in one integer parameter, the
# side length of a square, and returns the area. The function
# should be named find_area, and have one parameter:
# side_length.


# Write your function here!



# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "A square with side length 4 has an area of 16".

test_side_length = 4
print("A square with side length", test_side_length, "has an area of", find_area(test_side_length))


# Let's start with our function declaration. We know the
# function should be called find_area, and have one parameter:
# side_length. So, let's create that:

def find_area(side_length):
    # Now, we want to return the area of a square whose sides
    # are length side_length. This is just side_length
    # squared, so we could either do side_length ** 2 or
    # side_length * side_length. Let's do the first one.

    return side_length ** 2


# Now that we have that, we can test our code. When we run
# this file, it will print, "A square with side length 4
# has an area of 16".

test_side_length = 4
print("A square with side length", test_side_length, "has an area of", find_area(test_side_length))

# Notice that find_area() only returns the number 16: the
# rest of the text in the output comes from this print
# statement. Here we're demonstrating using a function
# inside another function's argument list (specifically,
# print()'s argument list).
