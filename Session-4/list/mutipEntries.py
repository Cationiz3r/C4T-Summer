
print()

entry = input("  Input Entries: ")

index = 0
entryList = [""]
for i in range(len(entry)):
    if entry[i] == ",":
        index += 1
        entryList.append("")
    else:
        entryList[index] += entry[i]

print()

for i in entryList:
    print(" ", i)

print()