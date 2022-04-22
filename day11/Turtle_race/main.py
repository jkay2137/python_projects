# Turtle race program
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make bet", prompt="Which turtle will win the race? Enter a color: ")
y_cor = -70
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
race_on = False


def move_to_start():
    global y_cor
    global colors
    global turtles
    i = 0
    for turtle in turtles:
        turtle.penup()
        turtle.color(colors[i])
        turtle.goto(x=-250, y=y_cor)
        y_cor += 30
        i += 1

for index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtles.append(turtle)

move_to_start()

if bet:
    race_on = True

while race_on:
    for temp_turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

        r = random.randint(0, 10)
        temp_turtle.forward(r)

screen.exitonclick()
