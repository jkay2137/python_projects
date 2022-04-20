from turtle import Turtle, Screen
import random
import colorgram

screen = Screen()
screen.bgcolor("black")
screen.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

x = 0
y = 0

turtle = Turtle()
turtle.speed(0)
turtle.color("white")
turtle.penup()
turtle.hideturtle()

def set_x_y():
    global x
    global y

    x = 0
    y += 50

def draw():
    for _ in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.penup()
        turtle.forward(50)
    set_x_y() 

for _ in range(10):
    turtle.setx(x)
    turtle.sety(y)
    draw()

screen.exitonclick()
