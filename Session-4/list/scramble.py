import random
import os

wordList = [
    "attorney",
    "audience",
    "author",
    "authority",
    "born",
    "both",
    "box",
    "boy",
    "break",
    "bring",
    "brother",
    "budget",
    "build",
    "building",
    "business",
    "but",
    "buy",
    "by",
    "call",
    "camera",
    "campaign",
    "friend",
    "from",
    "front",
    "full",
    "fund",
    "future",
    "game"
]


point = 0
correct = True

previous = []

while True:
    # Clear scr
    clear = lambda: os.system("cls")
    clear()

    print()
    print("  Point:", point, end=" ")

    if not correct:
        print("(Incorrect)", end="")
    print()
    print()

    print("   Unscramble: ", end = "")

    

    # Display Word
    if correct:
        wordIndex = random.randint(0, len(wordList) - 1)
        word = list(wordList[wordIndex])
        correct = False

        previous = []

        while word != []:
            length = len(word)
            index = random.randint(0, length - 1)
            print(word[index], end = " ")
            previous.append(word[index])
            word.pop(index)
    else:
        for i in previous:
            print(i, end = " ")


    print()

    

    # Answer
    print()
    answer = input("  Your answer: ")
    
    if answer == wordList[wordIndex]:
        correct = True
        point += 1
        