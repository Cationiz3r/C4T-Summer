
provinceLst = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
populationLst = [150300, 247100, 333300, 266800, 420900, 318000]
areaLst = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]

densityLst = []

for i in range(len(provinceLst)):
    densityLst.append(float("%.2f" % (populationLst[i] / areaLst[i])))

print()
print("  Average population density:", "%.2f" % (sum(densityLst) / len(densityLst)))
print()