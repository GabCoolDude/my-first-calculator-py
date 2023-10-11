
sign = input("What do you want to do? +, -, /, or *: ")
num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")
if sign == "+":
    result = int(num1) + int(num2)
if sign == "-":
    result = int(num1) - int(num2)
if sign == "*":
    result = int(num1) *  int(num2)
if sign == "/":
    result = int(num1) / int(num2)

print(int(result))