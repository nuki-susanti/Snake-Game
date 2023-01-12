import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import SCOREBOARD
from speed import SPEED


# 1. Setting up screen game
screen = t.Screen()
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0) # Turn off the animation so that snake bodies move in one unity


speed = SPEED()
speed.speed_choice()
level = screen.textinput('Type your level', 'Medium is the default')
speed.game_level(level)


# 2. Creating initial snake body
snake = Snake() # Creating snake
food = Food() # Calling food class
scoreboard = SCOREBOARD() # Calling scoreboard class

# 4. Controling the snake
screen.listen()
screen.onkey(snake.up, 'Up') # Up button will trigger snake_up function
screen.onkey(snake.down, 'Down') # Down button will trigger snake_down function
screen.onkey(snake.left, 'Left') # Left button will trigger snake_left function
screen.onkey(snake.right, 'Right') # Right button will trigger snake_right function

# 3. Moving the snake
game_on = True # Variable to control whether or not game is on -> snake is moving

while game_on:
    screen.update()
    time.sleep(speed.default_time_sleep)  # Updating the screen so that moving snake appears in one unity

    snake.move()
    # 6. Feeding on the food
    if snake.head.distance(food) < 15:
        food.create_food()
        snake.extend_snake() # Extending snake body everytime it feeds on the food
        scoreboard.update_scoreboard()

    # 7. Detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False # Game over when snake head hits the wall
        scoreboard.game_over()

    # 8. Detecting collision with its body
    for body in snake.snake_bodies[1:]: # Excluding the head
        if snake.head.distance(body) <= 5:
            game_on = False # Game over when snake head hit the wall
            scoreboard.game_over()
    
screen.exitonclick()
