import turtle
import pandas

states_data = pandas.read_csv("states.csv")
states = states_data.state.to_list()
counter = 0
screen = turtle.Screen()
screen.title("U.S. State Game")
good_answers = []    
img = "blank_states_img.gif"
df = pandas.DataFrame(good_answers)

screen.addshape(img)
turtle.shape(img)

def write(obj):
    data = states_data[states_data["state"] == obj]
    t = turtle.Turtle()
    
    t.hideturtle()
    t.penup()
    t.goto(float(data.x), float(data.y))
    t.write(obj, True)

while counter < 50:
    try: 
        answer = turtle.textinput(title=f"{counter}/50 States Correct", prompt="What's another state's name?").title()
    except AttributeError:
        df.to_csv("answers.csv")
        exit()

    if answer in states:
        counter += 1
        good_answers.append(answer)
        write(answer)

df.to_csv("answers.csv")
screen.exitonclick()