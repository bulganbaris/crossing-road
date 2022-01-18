from turtle import Turtle


class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("darkgreen")

    def starting_position(self):
        self.penup()
        self.sety(-170)
        self.setheading(90)

    def move(self):
        self.forward(20)




