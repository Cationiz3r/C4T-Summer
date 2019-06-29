
provinceLst = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
populationLst = [150300, 247100, 333300, 266800, 420900, 318000]


for i in range(len(populationLst)):
    if (populationLst[i] == max(populationLst)):
        maxInd = i +1
    elif (populationLst[i] == min(populationLst)):
        minInd = i +1

print()
print("  Max PoP Index:", maxInd)
print("  Min PoP Index:", minInd)
print()
