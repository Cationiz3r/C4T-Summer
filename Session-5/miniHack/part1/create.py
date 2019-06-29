
colors = ["blue", "red", "teal", "green"]

print()
print("  Our color list: ", end = "")
for i in range(len(colors)):
    if i < len(colors) -1:
        print(colors[i], end = ", ")
    else:
        print(colors[i])
print()

newColor = input("  Enter a new color: ")
colors.append(newColor)

print()
print("  Our new color list: ", end = "")
for i in range(len(colors)):
    if i < len(colors) -1:
        print(colors[i], end = ", ")
    else:
        print(colors[i])
print()


