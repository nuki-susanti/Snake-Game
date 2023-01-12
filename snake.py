from turtle import Turtle

STARTING_POINTS = [(0, 0), (-20, 0)] # Starting point of the inital snake body
MOVING_DISTANCE = 20 # Px of the snake is supposed to be moving
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_bodies = [] # A list to store the initial snake body and new snake bodies when it feeds on its food
        self.create_snake()
        self.head = self.snake_bodies[0]

    def create_snake(self): # Creating seed snake
        for point in STARTING_POINTS:
            self.add_snake_bodies(point)

    def add_snake_bodies(self, point): # Adding snake bodies
        seed_snake = Turtle()
        seed_snake.shape('square')
        seed_snake.color('white')
        seed_snake.penup()
        seed_snake.goto(point)
        self.snake_bodies.append(seed_snake)

    def extend_snake(self): # Extending the size of the snake at the back (tail) everytime it eats the food
        self.add_snake_bodies(self.snake_bodies[-1].position()) # Holding the tail position and adding the new body to the new position as the last tail

    def move(self):
        for body in range(len(self.snake_bodies)-1, 0, -1):
            new_x = self.snake_bodies[body - 1].xcor() # Getting the x coordinate of the body ahead 2 -> 1
            new_y = self.snake_bodies[body - 1].ycor() # Getting the y coordinate of the body ahead 2 -> 1
            self.snake_bodies[body].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: # Controlling movement, if snake facing down, it is not allowed to go backwards (up)
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: # Controlling movement, if snake facing up, it is not allowed to go backwards (down)
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT: # Controlling movement, if snake facing right it is not allowed to go backwards (left)
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT: # Controlling movement, if snake facing left, it is not allowed to go backwards (right))
            self.head.setheading(RIGHT)