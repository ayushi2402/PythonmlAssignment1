sf = input("Enter the name of the source file: ")
df = input("Enter the name of the destination file: ")

with open(sf, "r") as s:
    with open(df, "w") as d:
        d.write(s.read())

print("Contents copied from", sf, "to", df)
