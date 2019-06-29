
colors = ["blue", "red", "teal", "green"]

print()
print("  Our color list:")
for i in range(len(colors)):
    print("   ", i + 1, end = "")
    print(".", colors[i])

print()
deleteItem = input("  Item to delete: ")

if deleteItem.isnumeric():
    colors.pop(int(deleteItem) - 1)
else:
    colors.remove(deleteItem)

print()
print("  Our new color list:")
for i in range(len(colors)):
    print("   ", i + 1, end = "")
    print(".", colors[i])

print()
