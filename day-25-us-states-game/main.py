import turtle as t
from os import path

import pandas as p

DIRNAME = path.dirname(__file__)

screen = t.Screen()
screen.setup(width=750, height=500)
screen.title("U.S. States Game")
image = f"{DIRNAME}/blank_states_img.gif"
screen.addshape(image)
t.shape(image)
data = p.read_csv(f"{DIRNAME}/50_states.csv")
score = 0
states = {}
screen.tracer(0)

for i, row in data.iterrows():
    state_turtle = t.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto((float(row.x), float(row.y)))
    states[row.state.lower()] = {
        "turtle": state_turtle,
        "is_shown": False,
        "name": row.state,
    }


while score < 50:
    screen.update()
    answer_state = screen.textinput(
        title=f"{score}/50 States correct",
        prompt="What's another state's name?",
    )
    if answer_state:
        if answer_state.lower() == "exit":
            break
        elif answer_state.lower() in states:
            state_turtle = states[answer_state.lower()]
            if not state_turtle["is_shown"]:
                state_turtle["turtle"].write(state_turtle["name"])
                state_turtle["is_shown"] = True
                score += 1
