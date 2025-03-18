#   Turtle Movement
#   Cars Generation & Movement
#   Detect Collision with Car
# Detect when turtle reaches other side
# Create scoreboard
# Increase level & car speed


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tut = Player()
car_manager = CarManager()

screen.onkey(tut.move_front, 'Up')
screen.onkey(tut.move_back, 'Down')

i = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if i % 6 == 0:
        car_manager.create_car()
    
    car_manager.move_cars()
    
    for car in car_manager.all_cars:
        if tut.distance(car) < 20:
            game_is_on = False
    
    i += 1

screen.exitonclick()
