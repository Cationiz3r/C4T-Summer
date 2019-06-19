import turtle

t = turtle.Turtle()

print()
radius = int(input(" Input Radius: "))

for i in range(90):
    t.forward(radius /2 /3.141592)
    t.left(4)

turtle.mainloop()