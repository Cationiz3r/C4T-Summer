
numLst = [5, 1, 8, 92, 7, 30]
evenLst = []

for i in numLst:
    if i % 2 == 0:
        evenLst.append(i)

print()
print("  All even numbers:", end = " ")
for i in range(len(evenLst)):
    if i < len(evenLst) -1:
        print(evenLst[i], end = ", ")
    else:
        print(evenLst[i])
print()
