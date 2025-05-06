import time
import random
from turtle import Turtle, Screen
import scoreboard

WIDTH, HEIGHT = 800, 800
screen = Screen()
screen.screensize(WIDTH, HEIGHT)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('Black')
screen.title('Snake Game')
screen.tracer(0)

sb = scoreboard.ScoreBoard()
snake = []
snake_position = []
new_body_parts = []
apples = []

snake_alive = True
snake_direction = 'right'
snake_has_turned = False

snake_head = Turtle(shape='square')
snake_head.penup()
snake_head.turtlesize(1.1)
snake_head.color('Green')
snake_head.speed(1)
snake.append(snake_head)
snake_position.append((snake_head.xcor(), snake_head.ycor()))


def make_apple():
    apple = Turtle(shape='square')
    apple.penup()
    apple.turtlesize(0.5)
    apple.color('red')
    apple.setpos((random.randrange(-int((WIDTH/2)-20), int((WIDTH/2)-20), 20), random.randrange(-int((HEIGHT/2)-20), int((HEIGHT/2)-20), 20)))
    apples.append(apple)

def grow_snake():
    snake_body_part = Turtle(shape='square')
    snake_body_part.penup()
    snake_body_part.turtlesize(0.8)
    snake_body_part.color('Green')
    snake_body_part.speed(1)
    if len(snake) < 2:
        snake_body_part.setpos(snake_head.xcor(), snake_head.ycor())
    else:
        snake_body_part.setpos(snake[len(snake)-1].xcor(), snake[len(snake)-1].ycor())
    new_body_parts.append(snake_body_part)

def move_snake():
    if len(new_body_parts) > 0:
        nbp = new_body_parts[0]
        snake.append(nbp)
        snake_position.append(snake_position[len(snake_position)-1])
        new_body_parts.pop(0)

    if len(snake) == 1:
        snake_position[0] = (snake_head.xcor(), snake_head.ycor())
    else:
        for s in range(len(snake)-1, 0, -1):
            snake[s].setposition(snake_position[s-1])
            snake_position[s] = snake_position[s-1]
        snake_position[0] = (snake_head.xcor(), snake_head.ycor())


def move_head_forward():
    if snake_direction == 'right':
        snake[0].setposition(snake[0].xcor() + 20, snake[0].ycor())
    elif snake_direction == 'left':
        snake[0].setposition(snake[0].xcor() - 20, snake[0].ycor())
    elif snake_direction == 'up':
        snake[0].setposition(snake[0].xcor(), snake[0].ycor() + 20)
    elif snake_direction == 'down':
        snake[0].setposition(snake[0].xcor(), snake[0].ycor() - 20)
    global snake_has_turned
    snake_has_turned = False

def turn_right():
    global snake_direction
    snake_head.setheading(snake_head.heading() - 90)
    if snake_head.heading() == 0:
        snake_direction = 'right'
    elif snake_head.heading() == 90:
        snake_direction = 'up'
    elif snake_head.heading() == 180:
        snake_direction = 'left'
    elif snake_head.heading() == 270:
        snake_direction = 'down'
    snake_turn()

def turn_left():
    global snake_direction
    snake_head.setheading(snake_head.heading() + 90)
    if snake_head.heading() == 0:
        snake_direction = 'right'
    elif snake_head.heading() == 90:
        snake_direction = 'up'
    elif snake_head.heading() == 180:
        snake_direction = 'left'
    elif snake_head.heading() == 270:
        snake_direction = 'down'
    snake_turn()

def snake_turn():
    global snake_has_turned
    snake_has_turned = not snake_has_turned


def collision_detector():
    global snake_alive
    if -screen.canvwidth/2 >= snake_position[0][0] or snake_position[0][0] >= screen.canvwidth/2 or -screen.canvheight/2 >= snake_position[0][1] or snake_position[0][1] >= screen.canvheight/2:
        snake_alive = False
        print('You collided with a wall. Game Over.')
        print(f'Your final score was: {sb.score}')
        sb.game_over()
    for i in range(1, len(snake)-1):
        if snake_position[i] == snake_position[0]:
            snake_alive = False
            print('You collided with yourself. Game Over.')
            print(f'Your final score was: {sb.score}')
            sb.game_over()

    for a in apples:
        for bp in snake:
            if a.pos() == bp.pos():
                apples[0].reset()
                apples.pop(0)
                make_apple()
                grow_snake()
                sb.update_score()

screen.listen()
if not snake_has_turned:
    screen.onkeypress(turn_left, 'Left')
    # screen.onkeypress(snake_turn, 'Left')
    screen.onkeypress(turn_right, 'Right')
    # screen.onkeypress(snake_turn, 'Right')

grow_snake()
grow_snake()
make_apple()

while snake_alive:
    move_head_forward()
    move_snake()
    screen.update()
    collision_detector()
    time.sleep(0.1)


screen.exitonclick()


