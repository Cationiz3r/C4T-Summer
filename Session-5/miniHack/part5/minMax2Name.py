
provinceLst = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
populationLst = [150300, 247100, 333300, 266800, 420900, 318000]

for i in range(len(populationLst)):
    if (populationLst[i] == max(populationLst)):
        maxInd = i
    elif (populationLst[i] == min(populationLst)):
        minInd = i

print()
print("  Max PoP Name:", provinceLst[maxInd])
print("  Min PoP Name:", provinceLst[minInd])
print()
