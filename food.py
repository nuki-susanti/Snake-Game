import turtle as t
import random

COLORS = ['red', 'yellow', 'blue', 'white', 'grey', 'green', 'orange red', 'light sky blue', 'orchid', 'goldenrod']

class Food(t.Turtle): # Food class inherits all capabilities of Turtle class
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Size of the food 10 x 10 px (50% of the default 20 x 20)
        self.color(self.random_color())
        self.speed('fastest')
        self.create_food()

    def create_food(self): # Creating food
        self.color(self.random_color())
        random_gen_x = random.randint(-270, 270) # Random number from -270 to 270 as the screen is 600 x 600
        random_gen_y = random.randint(-270, 270) # Random number from -270 to 270 as the screen is 600 x 600
        self.goto(random_gen_x, random_gen_y)

    def random_color(self):
        color = random.choice(COLORS)
        return color

