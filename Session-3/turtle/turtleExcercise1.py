# Turtle Ex1

from turtle import *

t = Turtle()

t.fillcolor("yellow")
t.begin_fill()

for i in range(3):
    t.forward(300)
    t.left(120)
    
t.end_fill()

mainloop()