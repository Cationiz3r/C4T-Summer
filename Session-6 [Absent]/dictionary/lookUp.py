
colors = {
    "RED": "Hex: #FF0000",
    "GREEN": "Hex: #00FF00",
    "BLUE": "Hex: #0000FF",
    "MAGENTA": "Hex: #FF00FF",
    "CYAN": "Hex: 00FFFF",
    "YELLOW": "Hex: FFFF00",
    
    "ORANGE": "Hex: FF8000",
}

while True:
    print()
    color = input("  Input color: ")
    if color.upper() in colors:
        print("   ", colors[color.upper()])
    else:
        print("    Color doesn't exist (in current data)")
