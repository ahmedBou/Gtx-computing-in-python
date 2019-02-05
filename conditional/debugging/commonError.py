#Creates todaysWeather and sets it equal to "cold"
todaysWeather = "cold"

#Checks if todaysWeather equals "cold"
if todaysWeather == "cold":
    print("scarf")
print("Done!")
#Otherwise, checks if todaysWeather equals "windy" or "cold"
elif todaysWeather == "cold" or todaysWeather == "windy":
    print("jacket")
print("Done!")
#This else is unattached because the block
#was already broken!
else:
    print("t-shirt")
print("Done!")
