import msvcrt as m

for i in range(50):
    key = str(m.getch())
    # print(key == "d")
    print(i, key)