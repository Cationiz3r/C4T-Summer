# session 6

from datetime import *
from os import *

h = -1
while True:
    if not h == datetime.now().hour:
        clear = lambda: system("cls")
        clear()

        h= datetime.now().hour

        print()
        print("  The current hour is:", h)
        print()
