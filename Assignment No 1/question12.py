n = int(input("enter the numer/ "))
d = 0
while n>0:
    d = d + n%10
    n = int(n/10)

print("sum of digits of number: ",d)