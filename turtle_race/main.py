import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=400, width=500)

colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
bet = screen.textinput('Make your bet!', 'Choose the color of the turtle you want to bet on: ')
print(bet)

turtles = {}
def initialize_turtles(amount):
    margin = (screen.window_height()/(amount+1))
    for t in range(amount):
        name = colors[t-1]
        new_turtle = Turtle('turtle')
        new_turtle.penup()
        new_turtle.color(colors[t-1])
        turtles[name] = new_turtle
        new_turtle.setpos(x=-((screen.window_width()-40)/2), y=(t+1)*margin-(screen.window_height()/2))

def turtles_advance():
    for t in turtles:
        max_moved_dist = screen.window_width()-40
        turtle = turtles[t]
        x = turtle.xcor()
        y = turtle.ycor()
        moved_dist = random.randrange(int(max_moved_dist/10))
        turtle.setpos(x+moved_dist,y)

initialize_turtles(6)
not_in_goal = True
while not_in_goal:
    turtles_advance()
    for t in turtles:
        if turtles[t].xcor() >= (screen.window_width()/2)-20:
            print(f'The {turtles[t].pencolor()} won!')
            if turtles[t].pencolor() == bet:
                print('Congratulations, you won the bet!')
            else:
                print('You lost the bet.')
            not_in_goal = False

screen.listen()
screen.exitonclick()