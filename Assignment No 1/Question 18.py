str1 = input("Enter the first string: ").lower()
str2 = input("Enter the second string: ").lower()

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
