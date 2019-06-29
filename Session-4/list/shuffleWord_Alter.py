import random

print()
wordStr = input("Enter a Word: ")
print()

word = list(wordStr)

while word != []:
    length = len(word)
    index = random.randint(0, length - 1)
    print(word[index])
    word.pop(index)