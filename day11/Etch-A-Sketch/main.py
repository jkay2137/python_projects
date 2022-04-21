from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

def clear():
    turtle.home()
    turtle.clear()

def move_forward():
    turtle.forward(10)

def move_back():
    turtle.back(10)

def turn_right():
    turtle.right(10)

def turn_left():
    turtle.left(10)

screen.listen()

screen.onkey(fun=clear, key="c")
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")

screen.exitonclick()