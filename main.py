import time
from turtle import Screen
from tim import Tim
from drawers import Drawer
from cars import Car
from scoreboard import Scoreboard
from blood import Blood

screen = Screen()
screen.setup(width=600, height=400)
screen.title("Turtle Crossing")
screen.tracer(0)
car_speed = 10


tim = Tim()
tim.starting_position()
car = Car()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=tim.move)

top_line = Drawer(140)
bottom_line = Drawer(-100)
top_line.draw_lines()
bottom_line.draw_lines()

game_on = True


def car_motion():
    screen.update()
    car.create_traffic()
    car.move(car_speed)
    time.sleep(0.05)


while game_on:
    car_motion()

    for cars in car.traffic:
        if tim.distance(cars) < 24:
            blood = Blood(tim.xcor(), tim.ycor())
            tim.starting_position()
            scoreboard.reset()
            car_speed = 10
        if tim.ycor() > 140:
            tim.starting_position()
            car_speed += 1
            scoreboard.increment()
            print(car_speed)



























screen.exitonclick()