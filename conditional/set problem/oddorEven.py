n = int(input("enter your first number"))
"""b = int(input("enter your second number"))

if a % b == 0:
    print("the result is an even number")
else:
    print("the result is an odd number")
"""
if n % 2 != 0 or(n % 2 == 0 and 6 < n <= 20):
    print("Weird ")
elif n % 2 == 0 and (2 <= n <= 5 or n > 20):
    print("not weird ")
#elif n % 2 == 0 and 6 < n <= 20:
 #   print("Weird")