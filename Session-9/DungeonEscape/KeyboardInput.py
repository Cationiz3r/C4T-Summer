import msvcrt as m

for i in range(50):
    key = str(m.getch().decode("utf-8"))
    print(key, end = " ")