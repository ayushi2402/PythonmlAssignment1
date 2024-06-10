c = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ")
temp = float(input("Enter the temperature: "))

if c == 'C':
    f = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", f)
elif c == 'F':
    c = (temp - 32) * 5/9
    print("Temperature in Celsius:", c)
else:
    print("Invalid choice!")
