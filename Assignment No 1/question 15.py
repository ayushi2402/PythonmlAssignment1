import csv

f = input("Enter the name of the CSV file (with extension): ")

with open(f, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
