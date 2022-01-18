from turtle import Turtle, Screen

#Screen().tracer(0)


class Drawer(Turtle):
    def __init__(self, position_y):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.setheading(0)
        self.setx(-280)
        self.sety(position_y)

    def draw_lines(self):
        for n in range (0,10):
            self.forward(30)
            self.pendown()
            self.forward(30)
            self.penup()
