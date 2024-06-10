num = int(input("Enter the number whose factorial is to be calculated :"))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)
