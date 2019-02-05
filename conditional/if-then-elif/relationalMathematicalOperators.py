#Creates balance and sets it equal to 20.0
balance = 20.0
#Creates purchasePrice and sets it equal to 19.0
purchasePrice = 19.0
#Creates salesTax and sets it equal to 1.08
salesTax = 1.08

#Checks if balance is greater than or equal
#to purchasePrice times salesTax
if balance >= purchasePrice * salesTax:
    print("Purchase possible!")
else:
    print("Purchase not possible!")
print("Done!")