from turtle import Turtle

class Court(Turtle):
    PENSIZE = 5
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.draw_net_line()
        
    def draw_net_line(self):
        self.goto(0, 300)
        self.setheading(270)
        self.pendown()
        self.pensize(self.PENSIZE)
        for _ in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
        self.goto(0, -300)
    
    
        