# Creates a listsOfNumbers and assigns it to a list of ten numbers, 91 trough 100
listOfNumbers = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
sum = 0

# Runs this loop once for each item,assigning the current item to the var 'currentNumber'
"""
for currentNumber in listOfNumbers:
    sum += currentNumber
# Divides sum by the number of items in the list
print(sum / len(listOfNumbers))
"""
for i in range(0, len(listOfNumbers)):
    currentNumber = listOfNumbers[i]
    #print(listOfNumbers[i])
    #print(currentNumber)
    sum += currentNumber
    # print("sum inside of loop", sum)
print("sum in outside of loop",sum)
<qprint(sum / len(listOfNumbers))