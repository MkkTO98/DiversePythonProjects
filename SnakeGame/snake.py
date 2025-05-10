from turtle import Turtle

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.turtlesize(1.1)
        self.color('Green')
        self.speed(1)
        self.snake_body = []
        self.snake_position = []
        self.new_body_parts = []
        self.snake_body.append(self)
        self.snake_position.append((self.xcor(), self.ycor()))
        self.snake_direction = 'right'


    def grow_snake(self):
        snake_body_part = Turtle(shape='square')
        snake_body_part.penup()
        snake_body_part.turtlesize(0.8)
        snake_body_part.color('Green')
        snake_body_part.speed(1)
        if len(self.snake_body) < 2:
            snake_body_part.setpos(self.xcor(), self.ycor())
        else:
            snake_body_part.setpos(self.snake_body[len(self.snake_body) - 1].xcor(), self.snake_body[len(self.snake_body) - 1].ycor())
        self.new_body_parts.append(snake_body_part)
        del snake_body_part

    def move_snake(self):
        if len(self.new_body_parts) > 0:
            nbp = self.new_body_parts[0]
            self.snake_body.append(nbp)
            self.snake_position.append(self.snake_position[len(self.snake_position) - 1])
            self.new_body_parts.pop(0)
            del nbp

        if len(self.snake_body) == 1:
            self.snake_position[0] = (self.xcor(), self.ycor())
        else:
            for s in range(len(self.snake_body) - 1, 0, -1):
                self.snake_body[s].setposition(self.snake_position[s - 1])
                self.snake_position[s] = self.snake_position[s - 1]
            self.snake_position[0] = (self.xcor(), self.ycor())

    def move_head_forward(self):
        if self.snake_direction == 'right':
            self.snake_body[0].setposition(self.snake_body[0].xcor() + 20, self.snake_body[0].ycor())
        elif self.snake_direction == 'left':
            self.snake_body[0].setposition(self.snake_body[0].xcor() - 20, self.snake_body[0].ycor())
        elif self.snake_direction == 'up':
            self.snake_body[0].setposition(self.snake_body[0].xcor(), self.snake_body[0].ycor() + 20)
        elif self.snake_direction == 'down':
            self.snake_body[0].setposition(self.snake_body[0].xcor(), self.snake_body[0].ycor() - 20)

    def turn_right(self):
        self.setheading(self.heading() - 90)
        if self.heading() == 0:
            self.snake_direction = 'right'
        elif self.heading() == 90:
            self.snake_direction = 'up'
        elif self.heading() == 180:
            self.snake_direction = 'left'
        elif self.heading() == 270:
            self.snake_direction = 'down'

    def turn_left(self):
        self.setheading(self.heading() + 90)
        if self.heading() == 0:
            self.snake_direction = 'right'
        elif self.heading() == 90:
            self.snake_direction = 'up'
        elif self.heading() == 180:
            self.snake_direction = 'left'
        elif self.heading() == 270:
            self.snake_direction = 'down'



