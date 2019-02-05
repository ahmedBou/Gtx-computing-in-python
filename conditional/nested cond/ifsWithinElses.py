balance = 20.0
salesTax = 1.08
cardholderName = "David Joyner"
trustedVendors = ["Maria's", "Bob's", "Vrushali's", "Ling's", "Tias's"]
purchasePrice = 19.0
customerName = "David Joyner"
vendor = "Freddy's"
overdraftProtection = True

# This nested conditional checks whether the balance is less than or equal to the total of the price
# and the overdraft protection is not available; otherwise, whether the cardholder is not also the
# the customer; and otherwise, whether the vendor is not trusted.
if balance <= purchasePrice * salesTax and not overdraftProtection:
    print("Purchase not approved; no funds or overdraft protection.")
else:
    if not cardholderName == customerName:
        print("Purchase not approved; untrasted vendor.")
    else:
        if not vendor in trustedVendors:
            print("Purchase not approved; invalid customer.")
        else:
            print("Purchase approved!")
print("Done!")
"""
This nesting applies on both sides of the structure as well. We can write code that is functionally 
equivalent to the above with a completely different structure by nesting our conditionals in the else 
blocks instead
This code performs exactly the same, but all the nesting is inside the else portions of the conditional.
That’s because instead of checking whether the purchase passes each requirement on lines 15, 18, and 21,
it checks whether the purchase fails each requirement; notice how the logical expressions have changed
compared to Figure 3.2.20. If the purchase fails a condition, it prints that it’s failed and why; if not,
it moves on to the next check. This is like saying that a purchase is approved if none of the checks fail, 
rather than if all of them pass: these mean the same thing, but they’re organized a little differently.
"""