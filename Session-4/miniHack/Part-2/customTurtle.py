import turtle
t = turtle.Turtle()

print()
side = int(input("  Input side: "))
print()

for i in range(side):
    t.forward(1000 /side)
    t.left(360 /side)

turtle.mainloop()