import os

myList = ["C", "R", "U", "D"]

while True:
    clear = lambda: os.system("cls")
    clear()

    print()
    command = input("~$ ")
    command = command.upper()
    print()

    if command == "C":
        print("Your favourite thing:")
        fav = input("  ")
        myList.append(fav)

    if command == "R":
        if len(myList) == 0:
            print("(List is Empty)")
        else:
            for i in myList:
                print(i)
        
        input()

    if command == "U":
        pos = int(input("Update Pos: "))
        content = input("Updare Val: ")
        myList[pos -1] = content

    if command == "D":
        pos = int(input("Delete Pos: "))
        myList.pop(pos -1)

