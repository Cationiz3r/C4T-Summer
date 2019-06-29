
print()
myList = ["Movies", "Games", "Still-Games", "Games?", "Comics"]

found = False
for i in range(len(myList) -1, -1, -1):
    if myList[i] == "Games":
        myList.pop(i)
        found = True

if not found:
    print("That didn't exist..")
    print()

for i in myList:
    print(i, end = " ")

print(), print()