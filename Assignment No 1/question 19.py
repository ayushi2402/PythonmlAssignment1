import string

str1 = input()
str2 = str1.translate(str.maketrans("", "", string.punctuation))
print(str2)
