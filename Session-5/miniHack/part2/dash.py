import turtle
t = turtle.Turtle()

colors = ["blue", "red", "teal", "green"]

for i in range(len(colors)):
    t.pencolor(colors[i])
    t.forward(50)

turtle.mainloop()