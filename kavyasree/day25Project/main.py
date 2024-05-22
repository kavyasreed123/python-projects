import turtle
import pandas

# Initialize the turtle screen
screen = turtle.Screen()
screen.title("India States Game")
screen.setup(width=600, height=600)
image = "C:\\Users\\KDevaraju\\Documents\\newFolder\\pythonProjects\\projects\\day25Project\\india_blank_map.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Load the dataset containing state names
data = pandas.read_csv("C:\\Users\\KDevaraju\\Documents\\newFolder\\pythonProjects\\projects\\day25Project\\india_states.csv")
all_states = data.state.str.lower().to_list()

# List to store guessed states
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/35 states Correct",prompt="What's another state's name?")

    
    if answer_state == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    # Show the guessed state on the map
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state.str.lower() == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())  #(or) state_data.state.item()
    
screen.exitonclick()