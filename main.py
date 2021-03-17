import turtle as t
import pandas as pd


sf = pd.read_csv('50_states.csv')
sl = sf.state.tolist()
score = 0

scr = t.Screen()
scr.title('U.S. States Game')
scr.setup(width=750, height=500)
image = 'blank_states_img.gif'

scr.addshape(image)
t.shape(image)


def the_question():
    answer_state = scr.textinput(title='Guess the State ' + str(score) + '/50', prompt="What's another state's name?")

    if answer_state in sl:
        frame_index = sf[sf.state == answer_state].index[0]
        xcor = sf.x[frame_index]
        ycor = sf.y[frame_index]
        st = t.Turtle()
        st.penup()
        st.hideturtle()
        st.goto(xcor, ycor)
        st.write(answer_state)
        return 1
    else:
        return 0


while score < 50:
    score += the_question()


scr.exitonclick()
