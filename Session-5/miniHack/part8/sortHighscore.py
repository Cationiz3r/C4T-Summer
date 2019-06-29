
highLst = [45, 67, 56, 78]

highLst.sort(reverse = True)

print()
print("  High scores:")
for i in range(len(highLst)):
    print("   ", i +1, end = "")
    print(".", highLst[i])

print()
newHigh = int(input("  Enter your new score: "))

highLst.append(newHigh)
highLst.sort(reverse = True)

print()
print("  High scores:")
for i in range(len(highLst)):
    print("   ", i +1, end = "")
    print(".", highLst[i])

print()
