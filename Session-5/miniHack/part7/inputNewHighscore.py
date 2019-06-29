
highLst = [45, 67, 56, 78]

print()
print("  High scores:")
for i in range(len(highLst)):
    print("   ", i +1, end = "")
    print(".", highLst[i])

print()
newHigh = input("  Enter your new score: ")

highLst.append(newHigh)

print()
print("  High scores:")
for i in range(len(highLst)):
    print("   ", i +1, end = "")
    print(".", highLst[i])

print()
