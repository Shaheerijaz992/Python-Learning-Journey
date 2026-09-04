import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
screen.listen()
screen.onkey(player.move_up,"Up")
car_manager = CarManager()
car_manager.create_cars()
scoreboard = Scoreboard()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    if player.ycor() > FINISH_LINE_Y:
        scoreboard.increase_level()
        car_manager.increase_speed()
        scoreboard.update_score()
        player.goto_start()
    for car in car_manager.all_cars:
        if player.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
