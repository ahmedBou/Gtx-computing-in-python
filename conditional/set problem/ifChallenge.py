# Write a small program to ask for a name and age.
# when both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# if they are, welcome them to the holiday, otherwise print
# a (polite) message refuse them entry.
name = input("please enter your name")
age = int(input(f"{name}, enter your age please"))

if 18 <= age < 31:
    print(f"welcome to the holiday{name}")
else:
    print(f"Your age {age} can't let you enter to the holiday")
