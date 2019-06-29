
numList = [5, 1, 8, 92, 30]

print()
search = int(input("  Enter a number: "))

found = False
index = -1
for i in range(len(numList)):
    if search == numList[i]:
        found = True
        index = i
        break

print()
if found:
    print("  Found, position", index + 1)
else:
    print("  Not found in our list")
print()