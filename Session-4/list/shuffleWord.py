import random

print()
wordStr = input("Enter a Word: ")
print()

word = []
for i in wordStr:
    word.append(i)

swapTime = 100
for i in range(swapTime):
    a = random.randint(0, len(word) -1)
    b = random.randint(0, len(word) -1)
    word[a], word[b] = word[b], word[a]

for i in word:
    print(i.upper())
print()