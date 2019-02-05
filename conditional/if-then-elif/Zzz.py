mystery_string = "zizazzle"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The variable above creates a string. Add some code below
#that will print based on the maximum number of consecutive
#z's in the string:
#
# - If z appears three or more times in a row, print "I'm sleepy..."
# - If z appears two times in a row, print "I love ZZ Top!"
# - If z appears once, print "One is the loneliest number."
# - If z does not appear, print "Who needs z anyway?"
#
#The message you print should correspond to the most
#consecutive z's: in the original value of mystery_string,
#for example, you'd print "I love ZZ Top!" because there are
#two consecutive z's, even though there are also some
#individual z's.
#
#Ignore upper-case z's -- only look for lower-case z's.
#
#Hint: Remember the 'in' operator! It returns true if the
#first string is found within the second string. For example,
#"bog" in "boggle" would return True, but "bog" in "artemis"
#would return False.


#Add your code here!
if (3*"z") in mystery_string.lower():
    print("I'm sleepy...")
elif (2*"z") in mystery_string.lower():
    print("I love ZZ Top!")
elif ("z") in mystery_string.lower():
    print("One is the loneliest number.")
else:
    print("Who needs z anyway?")
###################################################################################

mystery_string = "zizazzle"

#There are a few things we need to notice here:
#
# - First, we need to check the strings in the right order:
#   if we check 'z' before checking 'zzz', we're guaranteed
#   to find 'z' even if 'zzz' is there.
# - Second, we need to use elif: once we've found something,
#   we want to stop. Otherwise if "zzz" was in the string,
#   it would print all three messages.
# - Third, we could take care of the case where there is no
#   'z' with an else, or with another elif if we use the
#   condition 'not "z" in mystery_string'.
#
#So, here's how we'd do it:

if "zzz" in mystery_string:
    print("I'm sleepy...")
elif "zz" in mystery_string:
    print("I love ZZ Top!")
elif "z" in mystery_string:
    print("One is the loneliest number.")
else:
    print("Who needs z anyway?")