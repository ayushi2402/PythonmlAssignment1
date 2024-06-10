num1 = float(input("Enter the first number: "))
o = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if o == '+':
    result = num1 + num2
elif o == '-':
    result = num1 - num2
elif o == '*':
    result = num1 * num2
elif o == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero is not allowed."
else:
    result = "Error! Invalid operator."

print("Result:", result)
