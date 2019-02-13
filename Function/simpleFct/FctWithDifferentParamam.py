#Defines the function "currencyAmount"
def currencyAmount(currency, amount):
    if currency == "JPY":
        return "¥" + str(amount)
    elif currency == "USD":
        return "$" + str(amount)
    elif currency == "GBP":
        return "£" + str(amount)
    else:
        return str(amount)

#Prints the output of currencyAmount("GBP", 5)
print(currencyAmount("GBP", 5))


####################################################
#Defines the function "returnYenAmount"
def returnYenAmount(amount):
    #Returns "¥"
    return "¥" + str(amount)

inputAmount = int(input("Enter the amount: "))
#Prints the output of returnYenAmount(inputAmount)
print(returnYenAmount(inputAmount))