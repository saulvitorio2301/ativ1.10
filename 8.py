import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(7)

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'black', 'red', 'orange']
for _ in range (12):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(30)
