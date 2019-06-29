
print()
numString = input("  Enter a list of numbers, separated by ' ': ")

numLst = []
prevNum = False
for i in numString:
    if i.isalnum() and (not prevNum):
        numLst.append(int(i))
        prevNum = True
    elif i.isalnum():
        numLst[len(numLst) -1] = numLst[len(numLst) -1] *10 +int(i)
    else:
        prevNum = False

print()
print("  Sum of all entered numbers:", sum(numLst))
print()
