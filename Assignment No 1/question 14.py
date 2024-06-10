l = []

print("Enter lines of text (enter an empty line to stop):")
while True:
    line = input()
    if line == "":
        break
    l.append(line)

print("\n".join(l))
