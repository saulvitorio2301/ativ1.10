import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(150)
    
turtle.backward(200)
turtle.right(90)

for _ in range(3):
  turtle.forward(150)
  turtle.left(90)
  
turtle.backward(275)
turtle.right(45)
turtle.backward(45)
turtle.forward(45)
turtle.left(45)
turtle.forward(475)
turtle.right(45)
turtle.backward(75)