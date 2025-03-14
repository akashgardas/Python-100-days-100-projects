from turtle import Turtle

FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)