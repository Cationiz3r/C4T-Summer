import os

character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2,
}

character["Gold"] += 50
character["Backpack"].append("FlintStone")
character["Pocket"] = ["MonsterDex", "Flashlight"]

skills = [
    {
        "Name": "Tackle",
        "Minimum level": 1,
        "Damage": 5,
        "Hit rate": 0.3,
    },
    {
        "Name": "Quick attack",
        "Minimum level": 2,
        "Damage": 3,
        "Hit rate": 0.5,
    },
    {
        "Name": "Strong Kick",
        "Minimum level": 4,
        "Damage": 9,
        "Hit rate": 0.2,
    },
]

while True:
    clear = lambda: os.system("cls")
    clear()

    print()
    for i in range(len(skills)):
        print("  Skill", i +1, end=": ")
        print(skills[i]["Name"])   
    print() 

    select= int(input("  Select Skill: "))

    if character["Level"] >= skills[select -1]["Minimum level"]:
        print("\n  Usable!")
    else:
        print("\n  Ununsable!")

    input()
