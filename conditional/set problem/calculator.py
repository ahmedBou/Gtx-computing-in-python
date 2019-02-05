num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
op = input("Enter the operator:")
if op == "+":
    print("result=", num1 + num2)
if op == "-":
    print("result:", num1 - num2)
if op == "/":
    print("result:", num1 / num2)
if op == "*":
    print("result:", num1 * num2)
if op == "**":
    print("result:", num1 ** num2)
if op == "%":
    print("result:", num1 % num2)
else:
    print("invalid operator")