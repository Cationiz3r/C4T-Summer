import os
import time
import random
import msvcrt as m

drawRange = {
    "X": {
        "Min": 0,
        "Max": 3,
    },
    "Y": {
        "Min": 0,
        "Max": 3,
    },
}
icons = {
    "Player": "P",
    "Key": "K",
    "Exit": "E",
    "Empty": "-",
    "Wall": "W",
    "Monster": "M"
}
message = [
    "You’ve just picked up a key!",
    "Congrats, you’ve just escaped the dungeon!",
    "You can't exit, please acquire the key(s) first!",
    "Victory!",
    "U died...",
]

playerData = {
    "BHealth": 8,
    "BDamage": 2, # Might use Move list or [Equip menu]
    "BDefend": 1,
    "Bags": [],

    # "CurHP": 8,
}
monstersData = [
    {
        "Name": "Eyebat",
        "Health": 3,
        "Damage": 1,
        "Defend": 0,
        "HitChance": 80,  # When this attack
        "MissChance": 75, # When player attack
        "RunChance": 90, # YEET Chance
    },
    {
        "Name": "Goblin",
        "Health": 4,
        "Damage": .8,
        "Defend": .5,
        "HitChance": 95,
        "MissChance": 80,
        "RunChance": 70,
    },
]

levelsData = [
    {
        "NeededKeys": 1,
        "Monsters": 0,
        "Items": 0,
        "ItemType": "(None)",
    },
    {
        "NeededKeys": 2,
        "Monsters": 0,
        "Items": 0,
        "ItemType": "(None)",
    },
    {
        "NeededKeys": 2,
        "Monsters": 1,
        "Items": 1,
        "ItemType": "Stats",
    },
    {
        "NeededKeys": 3,
        "Monsters": 1,
        "Items": 1,
        "ItemType": "Equipments",
    },
]
pickUpData = {
    "Stats": [
        {
            "Name": "Small Potion (Red)",
            "+HP": 5,
            # "+DP": 0,
            "Chance": 80,
        },
        {
            "Name": "Medium Potion (Red)",
            "+HP": 15,
            "Chance": 15,
        },
        {
            "Name": "Small Potion (Red)",
            "+HP": 50,
            "Chance": 5,
        },        
    ],
    "Equipments": [
        {
            "Name": "Light Helmet",
            "Defend": 1,
        },
    ],
}

menuNav = [
    {
        "Min": 0,
        "Max": 3,
        "Direct": [-1, -1, 1, -1]
    }
]

# QUICK GLOBAL INIT
clear = lambda: os.system("cls")
level = -1
messageID = -1
gameOver = False
inBattle = False

curHealth = 8


def quickCoord():
    return {
        "X": random.randint(drawRange["X"]["Min"], drawRange["X"]["Max"]),
        "Y": random.randint(drawRange["Y"]["Min"], drawRange["Y"]["Max"]),
    }

def differentCoord(item, checkList):
    dif = True
    for check in checkList:
        if (item["X"] == check["X"] and item["Y"] == check["Y"]):
            dif = False
            break
    return dif

def getDifferentCoord(checkList): 
    satisfied = False
    while not satisfied:
        newItem = quickCoord()
        satisfied = differentCoord(newItem, checkList)    
    return newItem

def showMes(n):
    global messageID
    messageID = n

def boundCoord(coord):
    if (coord["X"] < drawRange["X"]["Min"]):
        coord["X"] = drawRange["X"]["Min"]
    if (coord["Y"] < drawRange["X"]["Min"]):
        coord["Y"] = drawRange["X"]["Min"]
    if (coord["X"] > drawRange["X"]["Max"]):
        coord["X"] = drawRange["X"]["Max"]
    if (coord["Y"] > drawRange["X"]["Max"]):
        coord["Y"] = drawRange["X"]["Max"]

"""--------------------------------------------<RESET>--------------------------------------------"""
def reset(keyReset = 1, monsterReset = 1):
    global player, exitCoord, wall, keys, keyCollected, messageID, gameOver
    global option, menu
    global monsters
    
    # Define Keys
    keys = []
    for i in range(keyReset): 
        keys.append(getDifferentCoord(keys))
        keys[i]["Collected"] = False

    checkList = keys.copy()
    keyCollected = 0

    # print(keys)
    # print(checkList)
    
    player = getDifferentCoord(checkList)
    checkList.append(player)

    # print(checkList)
    # print(player)

    exitCoord = getDifferentCoord(checkList)
    checkList.append(exitCoord)

    wall = getDifferentCoord(checkList)

    # print(checkList)
    # print(exitCoord)

    # Defines monster
    monsters = []
    for i in range(monsterReset):
        monsters.append(getDifferentCoord(checkList))
        checkList.append(monsters[i]) # Save memory
        monsters[i]["Index"] = random.randint(0, len(monstersData) - 1)
        monsters[i]["Defeated"] = False

        # print(monsters[i])

    option = 0
    menu = 0
"""-------------------------------------------</RESET>--------------------------------------------"""

def advanceLevel(up = 1):
    global level 
    level += up
    reset(levelsData[level]["NeededKeys"], levelsData[level]["Monsters"])

def DisplayWorld():
    clear()

    global keys, player, exitCoord, monsters, messageID

    if (messageID != -1):
        print(message[messageID])        
        if (messageID == 1):
            # Endgame || Moregame
            # gameOver = True
            advanceLevel()

        messageID = -1
    else:
        print()

    for y in range(drawRange["Y"]["Max"] - drawRange["Y"]["Min"] + 1):
        for x in range(drawRange["X"]["Max"] - drawRange["X"]["Min"] + 1):
            keyHere = False
            for key in keys:
                if (x == key["X"] and y == key["Y"] and (not key["Collected"])):
                    print(icons["Key"], end = " ")
                    keyHere = True
                    break

            monsterHere = False
            for monster in monsters:
                if (x == monster["X"] and y == monster["Y"] and (not monster["Defeated"])):
                    print(icons["Monster"], end = " ")
                    monsterHere = True
                    break

            if (not (keyHere or monsterHere)):
                if (x == player["X"] and y == player["Y"]):
                    print(icons["Player"], end = " ")
                elif (x == exitCoord["X"] and y == exitCoord["Y"]):
                    print(icons["Exit"], end = " ")
                elif (x == wall["X"] and y == wall["Y"]):
                    print(icons["Wall"], end = " ")
                else:
                    print(icons["Empty"], end = " ")
        print()

def initBattle(upHP = 0, upATK = 0, upDFN = 0):  # Refresh Stats also
    global playerData, health, attack, defend

    health = playerData["BHealth"] + upHP
    attack = playerData["BDamage"] + upATK
    defend = playerData["BDefend"] + upDFN

def initMonster(index):
    return monstersData[index].copy()
    

def bar(ratio, length = 20, drawBrackets = True):
    if (drawBrackets):
        print("[", end = "")

    if (ratio <= 0):
        fill = 0
    else:
        fill = max([int(length * ratio), 1]) # Empty Bar + Still Alive = SUcc
    for i in range(fill):
        print("#", end = "")
    for i in range(length - fill):
        print(" ", end = "")

    if (drawBrackets):
        print("]", end = "")

def quickSelect(selection):
    global option
    if (option == selection):
        print(" > ", end="")
    else:
        print("   ", end="")

def changeMenu():
    pass

def DisplayBattle(noChoices = False):
    clear()

    global battleMonster, monsterCpy
    global player, health, attack, defend, curHealth
    global option, menu

    if (menu == 0):
        print(battleMonster["Name"], end = ": ")
        bar(battleMonster["Health"] / monsterCpy["Health"])
        print()

        # Player - Coord, PlayerData - Battle
        print("\nPlayer: ", end = "")
        bar(curHealth / health)
        print("  [", end = "")
        print(curHealth, "/", health, end = "]\n\n")

        if (not noChoices):
            quickSelect(0)
            print("Attack")
            quickSelect(1)
            print("Guard")
            quickSelect(2)
            print("Bag")
            quickSelect(3)
            print("Run")

def Display():
    if (inBattle):
        DisplayBattle()
    else:
        DisplayWorld()

def Input():
    global player, last, gameOver
    global enter, option

    key = str(m.getch())    

    if (inBattle): # Battle Input

        enter = False
        if (key == "b'\\r'"):
            
            enter = True

        key = key[2].upper()
        if (not enter):
            if (key == "w"):
                pass
            elif (key == "X"):
                gameOver = True

            elif (key == "W"):
                option -= 1
            elif (key == "S"):
                option += 1 

    else: # World Input
        # Last POS for Exit & Wall
        last = player.copy()

        # Current: No Enter Needed
        key = key[2].upper()
        if (key == "D"):
            player["X"] += 1
        elif (key == "A"):
            player["X"] -= 1
        elif (key == "S"):
            player["Y"] += 1
        elif (key == "W"):
            player["Y"] -= 1    

        elif (key == "X"):
            gameOver = True

def Logic():
    global gameOver
    global player, last, keys, keyCollected
    global inBattle, battleMonster, monsterCpy
    global curHealth, attack, defend
    global menu, option, enter, menuNav

    if (inBattle): # Battle Logic
        # Bound Option
        if (option < menuNav[menu]["Min"]):
            option = menuNav[menu]["Min"]
        if (option > menuNav[menu]["Max"]):
            option = menuNav[menu]["Max"]

        if (enter):
            if (menu == 0):
                if (option == 0):
                    battleMonster["Health"] -= max([attack - battleMonster["Defend"], 1])

                    DisplayBattle(True)
                    time.sleep(.4)

                    if (battleMonster["Health"] > 0):
                        curHealth -= max([battleMonster["Damage"] - defend, 1])
                    showMes(3)
        
        if (curHealth <= 0):
            print("...ded...")
            input()
            gameOver = True
        if (battleMonster["Health"] <= 0):
            for monster in monsters:
                if (player["X"] == monster["X"] and player["Y"] == monster["Y"] and (not monster["Defeated"])):
                    monster["Defeated"] = True
                    inBattle = False
                    break
    else:
        # Bound Player
        boundCoord(player)

        # Collect Key
        for key in keys:
            if (player["X"] == key["X"] and player["Y"] == key["Y"] and (not key["Collected"])):
                key["Collected"] = True
                keyCollected += 1

                showMes(0)

        # Check for Exit and Wall
        enoughKeys = (keyCollected == len(keys))
        if (player["X"] == exitCoord["X"] and player["Y"] == exitCoord["Y"]):
            if (enoughKeys):
                showMes(1)
            else:
                # player = last
                showMes(2)
        if (player["X"] == wall["X"] and player["Y"] == wall["Y"]):
            player = last

        # Init Battle!
        for monster in monsters:
            if (player["X"] == monster["X"] and player["Y"] == monster["Y"] and (not monster["Defeated"])):
                inBattle = True
                battleMonster = initMonster(monster["Index"])            
                monsterCpy = initMonster(monster["Index"])    



def main():
    global gameOver

    initBattle()
    advanceLevel(3) # Select Level ^ w^
    while not gameOver:
        Display()
        Input()
        Logic()
    
    clear()
    print()
    return 0

    # Debug
    # while True:
    #     Display()
    #     advanceLevel(0)
    #     input()

main()

