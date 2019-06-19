
print()

inStr = input("  Input: ")

print()

newStr = ""
for i in range(len(inStr)):
    newStr += inStr[i].capitalize()

print("  Capitalize:", newStr)
input()