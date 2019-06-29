
print()
myList = ["Movies", "Games", "Still Games", "Games?", "Comics"]

replace = input("Replace: ")
reContent = input("With: ")

print()

for i in myList:
    if i == replace:
        i = reContent
    print(i, end = " ")

print(), print()