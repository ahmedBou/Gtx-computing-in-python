#Sets up general information about the balance, tax, cardholder, and
#trusted vendors. Generally, the information in these lines would be
#sent into our program, not created here. Here, we create it manually
#to test out our code
balance = 20.0
salesTax = 1.08
cardholderName = "David Joyner"
trustedVendors = ["Maria's", "Bob's", "Vrushali's", "Ling's", "Tia's"]

purchasePrice = 19.0
customerName = "David Joyner"
vendor = "Vrushali's"

#This long conditional checks whether the balance is greater than the
#total price, whether the cardholder is also the customer, and whether
#the vendor is trusted.
if balance > purchasePrice * salesTax and cardholderName == \
        customerName and vendor in trustedVendors:
    print("Purchase approved!")
else:
    print("Purchase not approved!")
print("Done!")
###########################################################################
#Sets up general information about the balance, tax, cardholder, and
#trusted vendors. Generally, the information in these lines would be
#sent into our program, not created here. Here, we create it manually
#to test out our code
balance = 20.0
salesTax = 1.08
cardholderName = "David Joyner"
trustedVendors = ["Maria's", "Bob's", "Vrushali's", "Ling's", "Tia's"]

purchasePrice = 19.0
customerName = "David Joyner"
vendor = "Vrushali's"
overdraftProtection = True

#This long conditional checks whether the balance is greater than the
#total price or overdraft protection is available, whether the cardholder
#is also the customer, and whether the vendor is trusted.
if (balance > purchasePrice * salesTax or overdraftProtection) \
        and cardholderName == customerName and vendor in trustedVendors:
    print("Purchase approved!")
else:
    print("Purchase not approved!")
print("Done!")
