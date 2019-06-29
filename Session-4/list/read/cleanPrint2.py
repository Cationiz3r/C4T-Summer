
print()
myList = ["Games", "Games", "Games", "Games"]
for i in range(len(myList)):
    if i < len(myList) -1:
        print(myList[i], end = ", ")
    else:
        print(myList[i], end = "\n")        
print()