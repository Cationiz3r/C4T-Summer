import os

incString= "Not a correct answer :’("
corString= "Hura!!!"

current= 0
corCount= 0
continueAnyway= True
avoidZero = True


questions = [
    {
        "question": "How many legs does an octopus have?",
        "answers": ["One leg", "Two legs", "Four legs", "Eight legs"],
        "correct": 4,
    },
    {
        "question": "What is 23 * 16?",
        "answers": [248, 368, 298, 348],
        "correct": 2,
    },
    {
        "question": "1kg Diamond ? 1kg Steel",
        "answers": ["Heavier", "Lighter", "Same", "Undefined"],
        "correct": 3,
    },
    {
        "question": "1m3 Diamond ? 1m3 Steel",
        "answers": ["Heavier", "Lighter", "Same", "Undefined"],
        "correct": 2,
    },
    {
        "question": "Question index?",
        "answers": ["4", "5", "6", "7"],
        "correct": 1,
    },

    {
        "question": "",
        "answers": ["", "", "", ""],
        "correct": -1,
    },
]

while True:
    clear = lambda: os.system("cls")
    clear()

    print()
    print("  Correct answers:", corCount, end=" ")
    if not avoidZero:
        print("  [", "%.2f" % (corCount /current *100), "% ]\n")
    else:
        print("\n")
        avoidZero = False

    print(" ", questions[current]["question"], "\n")
    for i in range(len(questions[0]["answers"])):
        print("   ", i +1, end="")
        print(":", questions[current]["answers"][i])
        if i==3:
            print()

    answer= int(input("  Your answer: "))

    correct= answer == questions[current]["correct"]

    if correct:
        print("\n ", corString)
        current+= 1
        corCount+= 1
    else:
        print("\n ", incString)
        
        if continueAnyway:
            current+= 1

    input()
