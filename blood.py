from turtle import Turtle


class Blood(Turtle):
    def __init__(self, posx, posy):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=0.5)
        self.shape("circle")
        self.color("red")
        self.goto(posx, posy)
