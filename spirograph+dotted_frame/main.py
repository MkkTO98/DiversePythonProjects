import random
from turtle import Turtle, Screen, colormode
from random import randint
import colorgram
from PIL import Image

tim = Turtle()
colormode(255)
tim.shape('turtle')
tim.pensize(1)
tim.speed(0)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tim.color(r, g, b)

def random_color_from_img(img):
    colors = colorgram.extract(img, 10)
    rgb_colors = []
    for c in colors:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b
        rgb_colors.append((r,g,b))
    return rgb_colors

directions = [0, 90, 180, 270]
def random_direction():
    tim.setheading(random.choice(directions))


def make_spirograph(offset):
    for _ in range(int(360/offset)):
        rgb_colors = random_color_from_img(Image.open('tree.jpg'))
        tim.color(random.choice(rgb_colors))
        tim.circle(100)
        direction = tim.heading()
        tim.setheading(direction + offset)

def make_random_dotted_frame(height, width, dist):
    tim.penup()
    tim.setheading(0)
    for _ in range(height):
        for _ in range(width):
            random_color()
            tim.dot(dist/2)
            tim.forward(dist)
        tim.setheading(90)
        tim.forward(dist)
        tim.setheading(180)
        tim.forward(dist*width)
        tim.setheading(0)

def make_dotted_frame(height, width, dist):
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(320)
    tim.setheading(0)

    rgb_colors = random_color_from_img(Image.open('tree.jpg'))

    for _ in range(height):
        for _ in range(width):
            tim.color(random.choice(rgb_colors))
            tim.dot(dist / 2)
            tim.forward(dist)
        tim.setheading(90)
        tim.forward(dist)
        tim.setheading(180)
        tim.forward(dist * width)
        tim.setheading(0)

make_spirograph(10)

make_dotted_frame(10,10,50)

screen = Screen()
screen.exitonclick()
