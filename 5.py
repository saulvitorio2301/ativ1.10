import turtle
import random
turtle = turtle.Turtle()
colors = ['blue', 'black', 'green', 'yellow' ]
turtle.pensize(3)
for _ in [1, 2, 3]:
     color = random.choice(colors)
     turtle.color(color)
     turtle.forward(100)
     turtle.right(120)

for _ in [1, 2, 3, 4]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)