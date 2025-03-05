from turtle import Turtle, Screen
screen = Screen()

screen.tracer(8)
turtle = Turtle()
dist = 2
for i in range(200):
    turtle.fd(dist)
    turtle.rt(90)
    dist += 2

screen.exitonclick()