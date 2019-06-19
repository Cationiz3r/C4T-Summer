import os

# Same re, Length, PassCharacter, Email
error = False
cond = [True, True, True, True] 
while True:
    clear = lambda: os.system("cls")
    clear()

    print()

    if error:
        print("  Error:")
    if not cond[0]:
        print("    Password retype is not the same!")
    if not cond[1]:
        print("    Password is too short!")
    if not cond[2]:
        print("    Password must contain at least a number or a letter!")
    if not cond[3]:
        print("    Invaid Email!")
    if error:
        print()

    print("  Enter info:")
    username = input("    Username: ")
    password = input("    Password: ")
    repass = input("    Re-pass:  ")
    email = input("    Email:    ")

    # SameRE
    cond[0] = password == repass
    # LEngth
    # len>8, has letter, has number
    passCond = [False, False, False]
    passCond[0] = len(password) >= 8
    for i in range(len(password)):
        passCond[1] = passCond[1] or password[i].isalpha()
        passCond[2] = passCond[2] or password[i].isnumeric()
    cond[1] = passCond[0]
    cond[2] = passCond[1] and passCond[2]
    # Valid Email
    # Containing @ and .
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
    cond[3] = emailCond[0] and emailCond[1]

    error = not (cond[0] and cond[1] and cond[2] and cond[3])

    if not error:
        break

print()
    