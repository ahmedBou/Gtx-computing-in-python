def multiply(num1, num2):
    product = num1 * num2
    return product


multiply(4, 5)
print(product)
# The variable product is referenced from outside of its scope. correct

# Correct: Right! Any variable created inside the function can only be accessed by name from inside the
# function. If you need to access that variable's value outside the function, that's why we have the
# return operator! return product sends the value of product back out to where the function was called,
# but we need to store it somewhere. ( ) The result of multiply() is not stored anywhere.
# {{Close! You're right that this is probably a problem, but it won't cause an error.

# How can we fix that error?
# Set the result of multiply(4, 5) equal to a variable, then print that variable. correct

prod = multiply(4, 5)
print(prod)

# Correct: That's right! We could change line 4 to product = multiply(4, 5). Then product would exist
# on line 5. Note that even though they have the same name, the product declared on line 4 and the 
# product declared on line 2 would be different variables, like two different people with the same name.