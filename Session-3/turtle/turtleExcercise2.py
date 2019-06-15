# Turtle Ex1

from turtle import *

t = Turtle()

t.fillcolor("yellow")
t.begin_fill()

for i in range(90):
    t.forward(10)
    t.left(4)
    
t.end_fill()

mainloop()