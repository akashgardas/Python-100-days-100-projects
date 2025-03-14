from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.setposition(0, 260)
        self.write_score()
        self.update_score()
    
    def write_score(self):
        self.goto(-100, 260)
        self.write(self.l_score, align="left", font=("Courier", 30, "bold"))
        self.goto(100, 260)
        self.write(self.r_score, align="right", font=("Courier", 30, "bold"))
    
    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write_score()
        