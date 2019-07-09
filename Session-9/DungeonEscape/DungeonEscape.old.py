import os
import random

def randomAvoid(a, b, avoid = []):
    r = -1
    avoided = False
    while not avoided:
        avoided = True
        r = random.randint(a, b)

        for i in range(len(avoid)):
            # print(avoid[i], r)
            if (avoid[i] == r):
                avoided = False
                break
    
    return r        

def reset():
    global keyX, keyY, exitX, exitY, playerX, playerY, keyCollected
    keyX = random.randint(0, 3)
    keyY = random.randint(0, 3)
    exitX = randomAvoid(0, 3, [keyX])
    exitY = randomAvoid(0, 3, [keyY])
    playerX = randomAvoid(0, 3, [keyX, exitX])
    playerY = randomAvoid(0, 3, [keyY, exitY])
    keyCollected = False

keyX = random.randint(0, 3)
keyY = random.randint(0, 3)
exitX = randomAvoid(0, 3, [keyX])
exitY = randomAvoid(0, 3, [keyY])
playerX = randomAvoid(0, 3, [keyX, exitX])
playerY = randomAvoid(0, 3, [keyY, exitY])
keyCollected = False

message = [
    "You’ve just picked up a key!!!",
    "Congrats, you’ve just escaped the dungeon",
    "You can't exit, please acquire the key(s) first",
]
showMessage = False
messageID = -1

while True:
    # Draw
    clear = lambda: os.system("cls")
    clear()

    if (showMessage):
        print(message[messageID])
        showMessage = False
    else:
        print()

    for i in range(4):
        for j in range(4):
            if (j == keyX and i == keyY and (not keyCollected)):
                print("K", end = " ")
            elif (j == exitX and i == exitY):
                print("E", end = " ")
            elif (j == playerX and i == playerY):
                print("P", end = " ")
            else:
                print("-", end = " ")
        print()
    
    move = input("Your Move? ")

    # Last Pos
    lastX = playerX
    lastY = playerY

    # Input
    if (move.upper() == "D"):
        playerX += 1
    elif (move.upper() == "A"):
        playerX -= 1
    elif (move.upper() == "W"):
        playerY -= 1
    elif (move.upper() == "S"):
        playerY += 1

    # Logic
    if (playerX < 0):
        playerX = 0
    if (playerX > 3):
        playerX = 3
    if (playerY < 0):
        playerY = 0
    if (playerY > 3):
        playerY = 3

    if (playerX == keyX and playerY == keyY):
        keyCollected = True
        showMessage = True
        messageID = 0
    
    if (playerX == exitX and playerY == exitY):
        if (keyCollected):
            showMessage = True
            messageID = 1
        else:
            showMessage = True
            messageID = 2

            playerX = lastX
            playerY = lastY

    
        
    


    

