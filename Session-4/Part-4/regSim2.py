import os

same = True
while True:
    clear = lambda: os.system("cls")
    clear()

    print()

    if not same:
        print("  Error: Password retype is not the same!")
        print()


    print("  Enter info:")
    username = input("    Username: ")
    password = input("    Password: ")
    repass = input("    Re-pass:  ")
    email = input("    Email:    ")

    same = password == repass

    if same:
        break
        
print()
    