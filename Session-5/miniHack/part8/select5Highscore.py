
highLst = [45, 56, 67, 78,]
new = False

while True:

    # Sorting
    # highLst.sort(reverse = True)
    for i in range(len(highLst)):
        for j in range(i +1, len(highLst)):
            if highLst[i] < highLst[j]:
                highLst[i], highLst[j] = highLst[j], highLst[i]

    print()

    if not new:
        print("  ", end = "")
        new = True
    else:
        print("  NEW ", end = "")

    print("High scores:")
    for i in range(min([5, len(highLst)])):
        print("   ", i +1, end = "")
        print(".", highLst[i])

    print()
    newHigh = int(input("  Enter your new score: "))

    highLst.append(newHigh)

