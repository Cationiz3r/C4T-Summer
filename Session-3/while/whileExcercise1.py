# Validate String (name)
# Actually Session 6

# import os

numStr = "1234567890"

while True:
    print()
    # lambda: os.system("cls")

    pw= input("  Password: ")

    cond = False
    for i in range(len(pw)):
        for j in range(10):
            if pw[i]==numStr[j]:
                cond = True
                break
        if cond:
            break

    if cond:
        break

    print()
    print("  Error: Invalid password detected!")