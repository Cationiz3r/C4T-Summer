# :p

import os
import random

point = 0
randomWrong = 2
randomMath = 20
gameOver = False

tutorial = True
tText = "Correct[V]   Wrong[X]"

while not gameOver:
    clear = lambda: os.system("cls")
    clear()

    if tutorial:
        print()
        print("    ", tText)
        tutorial = False

    print()
    print("      Point :", point)
    print()

    plus = random.randint(0,1) == 0
    right = random.randint(0,1) == 0

    a = random.randint(1, randomMath)
    b = random.randint(1, randomMath)

    if plus:
        opper = "+"
        res = a + b
    else:
        opper = "-"
        res = a - b

    offset = 0
    if not right:
        while offset == 0:
            offset = random.randint(-randomWrong, randomWrong)
        
        res += offset

    print("           [ ", a, opper, b, "=", res, " ]")
    print()

    ans = input("                  ")

    if ans.upper() == "V" and right:
        point += 1
    elif ans.upper() == "X" and (not right):
        point += 1
    else:
        gameOver = True

clear()
print()
print("      Point :", point)
print()
print("             [ Game Over ]")

input()
