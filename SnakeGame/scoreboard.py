from turtle import Turtle, Screen

HEIGHT = 800

score = 0
score_pen = Turtle()
score_pen.color('white')
score_pen.speed(0)
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 3*HEIGHT/8)
score_pen.write(f'Score: {score}', align='center', font=('Arial', 20, 'bold'))

class ScoreBoard:
    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        score_pen.clear()
        score_pen.goto(0, 3 * HEIGHT / 8)
        score_pen.write(f'Score: {score}', align='center', font=('Arial', 20, 'bold'))

    def game_over(self):
        game_over_pen = Turtle()
        game_over_pen.color('white')
        game_over_pen.speed(0)
        game_over_pen.penup()
        game_over_pen.hideturtle()
        score_pen.goto(0, 0)
        score_pen.clear()
        score_pen.write('Game Over', align='center', font=('Arial', 100, 'bold'))
        score_pen.goto(0, -3 * HEIGHT / 8)
        score_pen.write(f'Final Score: {score}', align='center', font=('Arial', 50, 'bold'))