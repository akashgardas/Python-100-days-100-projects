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
scoreboard = ScoreBoard()

screen.onkey(tut.move_front, 'Up')
screen.onkey(tut.move_back, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with car
    for car in car_manager.all_cars:
        if tut.distance(car) < 20:
            game_is_on = False
    
    # Detect when turtle reaches other side
    if tut.is_at_finish_line():
        tut.reset()
        car_manager.increase_speed()
        scoreboard.increase_level()
        
scoreboard.game_over()
screen.exitonclick()
