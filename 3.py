import turtle

turtle = turtle.Turtle()
turtle.shape('turtle')  
turtle.pensize(5)  


for color in ['black', 'blue', 'red','pink' ]:
    turtle.color(color)
    for _ in range(4):  
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()
    turtle.forward(150) 
    turtle.pendown()