
provinceLst = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
populationLst = [150300, 247100, 333300, 266800, 420900, 318000]

maxVal = -1
for i in range(len(populationLst)):
    if populationLst[i] > maxVal:
        maxVal = populationLst[i]
        maxInd = i
minVal = maxVal
minInd = maxInd
for i in range(len(populationLst)):
    if populationLst[i] < minVal:
        minVal = populationLst[i]
        minInd = i

print()
print("  Max PoP Index:", maxInd + 1)
print("  Min PoP Index:", minInd + 1)
print()
