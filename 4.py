import turtle
import random

turtle = turtle.Turtle()
colors = ['black', 'purple', 'green', 'yellow']
turtle.pensize(7)

for _ in [1, 2, 3, 4]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.left(120)
