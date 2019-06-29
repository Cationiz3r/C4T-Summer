
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

print()
for i in range(len(skills)):
    print("  Skill", i +1, end=":\n")
    for k,v in skills[i].items():
        print("   ", k, end=": ")
        print(v)
    print()