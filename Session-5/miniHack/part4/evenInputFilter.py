
print()
numString = input("  Enter a list of numbers, separated by ‘,’: ")

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

evenLst = []
for i in numLst:
    if i % 2 == 0:
        evenLst.append(i)


print()
print("  All even numbers:", end = " ")
for i in range(len(evenLst)):
    if i < len(evenLst) -1:
        print(evenLst[i], end = ", ")
    else:
        print(evenLst[i])
print()
