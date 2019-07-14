import random
import os

def calChance(chance, total = 100):
    return random.randrange(total) + 1 <= chance

clear = lambda: os.system("cls")
satisfied = 0
total = 0
for i in range(5000):
    clear()

    if (calChance(50)):
        satisfied += 1
    total += 1

    print("%.4f" % (satisfied / total))