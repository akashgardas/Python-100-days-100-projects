from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'purple', 'blue', 'green', 'gray']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()
    
    def create_car(self):
        if random.randint(1, 6) != 1:
            return
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-250, 250))
        self.all_cars.append(car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -340:
                self.all_cars.remove(car)
            
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
