from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

'''Initializes screen and sets to width and height to 600 & 600,background color to black,
    title to Snake game
    screen.tracer(0) sets not to update screen until we specify so'''
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

'''Creates a snake(which has 3 body segments of turtle objects,
    creates a food Turtle object at rando location
    initilizes displying score'''
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


'''screen.listen() starts listening to key strokes and 
    takes desictions based on keys given'''
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,'Right')


def is_food_in_snake():
    """returns True if generated food object is in body of snake segments
        or returns False if food object is generated some where else"""
    for i in range(len(snake.snake)):
                if snake.snake[i].distance(food) < 15:
                    return True
    return False                
is_it_true = True

is_game_on = True
while is_game_on:
    '''Starts updating screen and time.sleep() puts the speed of snake
        which determines difficulty and starts moings the snake forward'''
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    '''here this block of code checks if the head of the snake has come in 
        contact with food.if yes snake segments extend by one point 
        and food is updated with different point on the screen'''
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()

        '''here if the newl generated food is in body of snake then 
        it keepsrefreshing food's location until it finds a location that is not on snake's body'''
        while is_it_true:
            if is_food_in_snake():
                food.refresh()
                is_it_true = True
            else:
                is_it_true = False 
        
        '''here score is incremented by 1 saying food has benn eaten and refreshes the score number on screen'''
        scoreboard.score += 1
        scoreboard.refresh_score()   

    '''here this if statement is checking if the head of the snake is gone over
        game window or hit an invisible wall which displas GAME OVER and terminates games'''
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on = False

    '''here this block of code is checking if head of the snake is colliding with
        its own body part,if it hits then game terminates and displays final score and text GAME OVER'''
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            is_game_on = False
            scoreboard.game_over()



screen.exitonclick()