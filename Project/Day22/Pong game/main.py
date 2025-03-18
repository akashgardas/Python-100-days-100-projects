# break down of the problem
# -     Create the screen
# -     Moving ball
# -     Detect collision with wall and bounce
# -     Detect collision with paddle
# -     Create paddles
# -     Moving paddles
# - Scores

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard
from court import Court

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # To turn off the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-360, 0))

ball = Ball()

scoreboard = ScoreBoard()
court = Court()

screen.listen()
# right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
    
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

screen.exitonclick()
