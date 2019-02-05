# Creates sum with the value 0
sum = 0
# Get the number of numbers to average
numCount = int(input("How many numbers will you average?"))
for i in range(1, numCount+1):
    # Gets the user's number
    nextNumber = int(input("Enter number #" + str(i)+": "))
    sum += nextNumber
# Print the sum over 10
print(sum)
print(numCount - 5)
print(f"{sum} / {numCount-5} = ", sum/numCount-5)