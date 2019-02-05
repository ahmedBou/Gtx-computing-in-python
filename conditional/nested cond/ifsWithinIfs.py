balance = 20.0
salesTax = 1.08
cardholderName = "David Joyner"
trustedVendors = ["Maria's", "Bob's", "Vrushali's", "Ling's", "Tias's"]
purchasePrice = 19.0
customerName = "David Joyner"
vendor = "Freddy's"
overdraftProtection = True

# This nested conditional checks whether the balance is greater than the total price or overdraft
# protection is available, then whether the cardholder is the customer, and then whether the vendor is
# trusted
if balance > purchasePrice * salesTax or overdraftProtection:
    if cardholderName == customerName:
        if vendor in trustedVendors:
            print("purchase is approved ")
        else:
            print("Purchase not approved; untrusted customers")
    else:
        print("Purchase not approved; invalid customers")
else:
    print("Purchase not approved, no funds or overdraft protection.")
print('Done!')
"""
Remember how we had to break one line of code between two lines just for readability in Figure 3.2.16?
With these nested conditionals, we no longer have to do that. Instead, we have three short, simple
conditional statements, one under the other on lines 14, 15, and 16. Each is indented under the previous 
one, meaning each only runs if the previous one also ran. That means the purchase is only approved if the
first conditional and the second conditional and the third conditional are all True, which makes it 
functionally equivalent to our original statement.
However, with this structure, each individual conditional can have its own dedicated else block, meaning
we can print exactly why the purchase failed. On line 8, I’ve changed the vendor to an untrusted vendor,
and so the code runs until it checks the third conditional on line 16. This condition is False, so it
jumps to this conditional’s else block (line 19) and says the vendor was untrusted. This tells us a lot 
more than our earlier code: it tells us the vendor was untrusted, and the fact that it reached this line 
also tells us that both the balance was
sufficient and the cardholder was valid because this conditional was controlled by those previous 
conditionals.
"""