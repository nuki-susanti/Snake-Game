from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 18, 'bold')

class SCOREBOARD(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color('white')
        self.hideturtle()
        self.scoreboard()


    def scoreboard(self):
        self.write(f'Your Score: {self.score}',align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.score += 1 # Increase by 1 when food is eaten by the snake
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(0,80)
        self.write(f'GAME OVER',align=ALIGN, font=FONT)

