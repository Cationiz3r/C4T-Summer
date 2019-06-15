# Validate String (name)
# Actually Session 6

# import os

numStr = "1234567890"

while True:
    print()
    # lambda: os.system("cls")

    name= input("  Name: ")

    cond = True
    for i in range(len(name)):
        for j in range(10):
            if name[i]==numStr[j]:
                cond = False
                break
        if not cond:
            break

    if cond:
        break

    print()
    print("  Error: Invalid name detected!")