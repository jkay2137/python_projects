# Turtle race program
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make bet", prompt="Which turtle will win the race? Enter a color: ")
y_cor = -100
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def move_to_start():
    global y_cor
    global colors
    global turtles
    i = 0
    for turtle in turtles:
        turtle.penup()
        turtle.color(colors[i])
        turtle.goto(x=-250, y=y_cor)
        y_cor += 50
        i += 1

red_turtle = Turtle(shape="turtle")
turtles.append(red_turtle)

orange_turtle = Turtle(shape="turtle")
turtles.append(orange_turtle)

yellow_turtle = Turtle(shape="turtle")
turtles.append(yellow_turtle)

green_turtle = Turtle(shape="turtle")
turtles.append(green_turtle)

blue_turtle = Turtle(shape="turtle")
turtles.append(blue_turtle)

purple_turtle = Turtle(shape="turtle")
turtles.append(purple_turtle)

move_to_start()


screen.exitonclick()
