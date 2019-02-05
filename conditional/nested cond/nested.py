"""
x=4
if x > 5:
    print("x is greater than 5.")
    if x > 0:
        print("x is greater than 0.")

if x > 5:
    print("x is greater than 5.")
if x > 0:
    print("x is greater than 0.")

if desiredShirt in cleanShirts and weather == "raining" and raincoatClean == True:
    print("Yes!")
if desiredShirt in cleanShirts:
    if weather == "raining":
        if raincoatClean == True:
            print(" Yes the raincoat is clean")

time = 2359
tirednessLevel = 90
homeworkDone = True
earlyClass = False

if time >= 2300:
    if tirednessLevel >= 85:
        if homeworkDone:
            if earlyClass:
                print("Go to sleep!")
            else:
                print("Go to sleep soon...")
        else:
            print("Finish your work, then sleep!")
    else:
        print("Stay up a little longer!")
else:
    print(" It's still pretty early.")

sunny = False
windy = False

if sunny:
    if not windy:
        print("wear a hat!")
    else:
        print("Enjoy the breeze")

accepted = ["Alex", "Bailey", "Chris", "Danielle"]
wait_list = ["Evan", "Faith", "George"]
myName = "Heather"
if myName in accepted:
    print("Welcome to Georgia Tech!")
else:
    if myName in wait_list:
        print("You're on the waitlist! Good luck.")
    else:
        print("Sorry, you haven't been accepted.")

entered = "abc123"
password = "abc123"
tries = 3
if entered == password and tries <= 3:
    print("Login Successful")
else:
    if entered != password and tries <= 3:
        print("Incorrect password")
    else:
        print("Tries exceeded")
"""