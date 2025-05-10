from turtle import Turtle, Screen


class ScoreBoard(Turtle):
    def __init__(self, height):
        super().__init__()
        self.height = height
        self.color('white')
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.score = 0
        with open('data.txt', 'r') as file:
            content = int(file.read())
            self.high_score = content
        self.snake_alive = True


    def write_score(self):
        self.clear()
        self.goto(0, 3 * self.height / 8 +30)
        self.write(f'High Score: {self.high_score}', align='center', font=('Arial', 12, 'bold'))
        self.goto(0, 3 * self.height / 8)
        self.write(f'Score: {self.score}', align='center', font=('Arial', 20, 'bold'))

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 100, 'bold'))
        self.goto(0, -3 * self.height / 8 +60)
        if self.score > self.high_score:
            self.write(f'NEW High Score: {self.score}', align='center', font=('Arial', 50, 'bold'))
        else:
            self.write(f'Final Score: {self.score}', align='center', font=('Arial', 50, 'bold'))

    def press_space(self):
        self.goto(0, -3 * self.height / 8 + 30)
        self.write('Press \'space\' to play a New Game.', align='center', font=('Arial', 20, 'normal'))