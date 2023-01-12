from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 18, 'bold')

class SPEED(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.default_time_sleep = 0.5

    def speed_choice(self):
        self.goto(0, 120)
        self.write('Select Your Level!', align=ALIGN, font=FONT)
        self.goto(0, 80)
        self.write("Type 'E' for Easy, 'M' for Medium or 'H' for Hard", align=ALIGN, font=FONT)

    def game_level(self, level):
        if level.lower() == 'e':
            self.default_time_sleep = 1
        elif level.lower() == 'h':
            self.default_time_sleep = 0.1
        else:
            self.default_time_sleep = 0.5

        self.clear()

       

        
        