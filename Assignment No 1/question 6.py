file = input("Enter the name of the text file: ")

with open(file, "r") as f:
    content = f.read()

print("Content of", file+ ":")
print(content)
