
print()
myList = ["Movies", "Games", "Still-Games", "Games?", "Comics"]

rem = int(input("Remove Index: "))
myList.pop(rem)
print()

for i in myList:
    print(i, end = " ")

print(), print()