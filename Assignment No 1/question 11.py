n = int(input("Enter the number to generate it's fibonacci : "))
f =[0,1]
for i in range(2,n):
    nn = f[-1]+f[-2]
    f.append(nn)

print("The fibonacci Series for given number will be:",f)
