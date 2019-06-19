cond = [True, True, False]
while True:
    email = input()
    emailCond = [False, False]
    start = -1
    for i in range(len(email)):
        if (email[i] == "@"):
            emailCond[0] = True
            start = i
            break
    if emailCond:
        for i in range(start, len(email)):
            if (i > start +1 and i < len(email) -1 and email[i] == "."):
                emailCond[1] = True
                break
    cond[2] = emailCond[0] and emailCond[1]

    print(cond[2])