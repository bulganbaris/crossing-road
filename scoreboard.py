from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_score()

    def create_score(self):
        self.hideturtle()
        self.penup()
        self.sety(170)
        self.write(f"Level: {self.score}", align="center", font=('Helvetica', 16, 'normal'))

    def increment(self):
        self.clear()
        self.score += 1
        self.create_score()

    def reset(self):
        self.clear()
        self.score = 0
        self.create_score()



