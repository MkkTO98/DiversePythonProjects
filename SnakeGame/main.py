import time
import random
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from snake import Snake

WIDTH, HEIGHT = 800, 800


def make_apple(apples):
    apple = Turtle(shape='square')
    apple.penup()
    apple.turtlesize(0.5)
    apple.color('red')
    apple.setpos((random.randrange(-int((WIDTH/2)-20), int((WIDTH/2)-20), 20), random.randrange(-int((HEIGHT/2)-20), int((HEIGHT/2)-20), 20)))
    apples.append(apple)


def collision_detector(snake, screen, apples):
    global pressed_space
    if -screen.canvwidth/2 >= snake.snake_position[0][0] or snake.snake_position[0][0] >= screen.canvwidth/2 or -screen.canvheight/2 >= snake.snake_position[0][1] or snake.snake_position[0][1] >= screen.canvheight/2:
        sb.snake_alive = False
        pressed_space = False
        print('You collided with a wall. Game Over.')
        print(f'Your final score was: {sb.score}')
        sb.game_over()
        sb.press_space()

    for i in range(1, len(snake.snake_body)-1):
        if snake.snake_position[i] == snake.snake_position[0]:
            sb.snake_alive = False
            pressed_space = False
            print('You collided with yourself. Game Over.')
            print(f'Your final score was: {sb.score}')
            sb.game_over()
            sb.press_space()

    for a in apples:
        for bp in snake.snake_body:
            if a.pos() == bp.pos():
                apples[0].reset()
                apples.pop(0)
                make_apple(apples)
                snake.grow_snake()
                sb.increase_score()

def play_new_game():
    global pressed_space
    sb.snake_alive = True
    pressed_space = True
    print('You pressed space to restart the game')

def play_game(screen_width, screen_height):

    apples = []
    screen = Screen()
    screen.setup(screen_width, screen_height)
    screen.screensize(screen_width, screen_height)
    screen.bgcolor('Black')
    screen.title('Snake Game')
    screen.tracer(0)

    snake = Snake()
    snake.grow_snake()
    snake.grow_snake()

    screen.listen()
    screen.onkeypress(snake.turn_left, 'Left')
    screen.onkeypress(snake.turn_right, 'Right')
    screen.onkeypress(play_new_game, 'space')


    while sb.snake_alive and not pressed_space:
        sb.write_score()
        sb.press_space()
        screen.update()
        time.sleep(0.5)
        sb.write_score()
        screen.update()
        time.sleep(0.5)

    make_apple(apples)

    while sb.snake_alive:
        snake.move_head_forward()
        snake.move_snake()
        collision_detector(snake, screen, apples)
        screen.update()
        time.sleep(0.1)

    while not sb.snake_alive and not pressed_space:
        sb.write_score()
        sb.game_over()
        sb.press_space()
        screen.update()
        time.sleep(0.5)
        sb.write_score()
        sb.game_over()
        screen.update()
        time.sleep(0.5)
    if sb.high_score < sb.score:
        sb.high_score = sb.score
        with open('data.txt', 'w') as file:
            file.write(f'sb.high_score')

    screen.clear()
    del screen

    sb.score = 0
    sb.write_score()
    return

sb = ScoreBoard(HEIGHT)
pressed_space = False

while True:
    play_game(WIDTH, HEIGHT)


