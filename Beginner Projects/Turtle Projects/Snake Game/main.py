from turtle import Turtle
from turtle import Screen

from scoreboard import Scoreboard
from food import Food
import time
from Snake import Snake
snake = Snake()
food = Food()
screen = Screen()
scoreboard =Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect Collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        scoreboard.reset()
        snake.reset()
    #Detect Collisions with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()