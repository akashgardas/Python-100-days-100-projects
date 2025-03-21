from turtle import Turtle

FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=FONT)
    