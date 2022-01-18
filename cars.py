from turtle import Turtle
import random

CAR_COLORS = ["orange", "teal", "purple", "pink", "gray", "green"]
SPAWN_POINTS = [-80, -20, 40, 100, 160]


class Car:
    def __init__(self):
        self.traffic = []

    def create_traffic(self):
        dice = random.randint(0, 6)
        if dice == 3:
            car = Turtle()
            car.speed(1)
            car.penup()
            car.setx(-350)
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(CAR_COLORS))
            car.sety(random.randrange(-90, 120, 30))
            self.traffic.append(car)

    def move(self, speed):
        for cars in self.traffic:
            cars.forward(speed)

















