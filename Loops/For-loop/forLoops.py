number = "9,223,372,036,854,775,807"
cleanNumber = ''
for i in range(0, len(number)):
    # if number[i] != ",":
    #     print(number[i])
    # or
    if number[i] in "0123456789":
        cleanNumber += number[i]
newNumber = int(cleanNumber)
print(f"the number is {newNumber}")

# more readable :
for char in number:
    if char in "0123456789":
        cleanNumber += char
newNumber = int(cleanNumber)
print(f"The number is {newNumber}")

# 2nd example:
for state in ["not good", "no more", " a stiff", "bereft of life"]:
    print("This parrot is " + state)
# range
for i in range(0, 100, 5):
    print(i)
# times
for i in range(1, 14):
    for j in range(1, 14):
        print(f"{i} times {j} is: {i*j}", end='\t')
    print(30 * "=")