s = input("Enter a string: ")
p = input("Enter the prefix to check: ")
suf = input("Enter the suffix to check: ")

if s.startswith(p):
    print("String starts with the prefix.")
else:
    print("String does not start with the prefix.")

if s.endswith(suf):
    print("String ends with the suffix.")
else:
    print("String does not end with the suffix.")
