# Turtle Ex1

from turtle import *

t = Turtle()

t.pencolor("green")

for i in range(6):
    for j in range(60):
        t.forward(10)
        t.left(6)    
    t.left(60)

mainloop()