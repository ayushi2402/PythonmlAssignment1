text = input("Enter the text you want to write to the file: ")
file_name = input("Enter the file name (with extension): ")

with open(file_name, "w") as file:
    file.write(text)

print("Text has been written to", file_name)
