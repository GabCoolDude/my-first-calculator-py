print("We can add, subtract, multiply and divide")
sign = input("What do you want to do? +, -, /, or *: ")
while sign != "+" "-" "/" "*":
    sign = input("Please enter a correct sign : ")

num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")
if sign == "+":
    result = float(num1) + float(num2)
if sign == "-":
    result = float(num1) - float(num2)
if sign == "*":
    result = float(num1) *  float(num2)
if sign == "/":
    result = float(num1) / float(num2)

print(result)