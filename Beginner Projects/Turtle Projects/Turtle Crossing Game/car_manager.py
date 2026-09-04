import scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
LANES = [-200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200]

class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.speed=5

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(1,2)
        car.penup()
        car.goto(random.randrange(-250,250),random.choice(LANES))
        self.all_cars.append(car)
    def create_cars(self):
        for i in range(6):
            self.create_car()
    def move_cars(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.speed)
            car.speed("fastest")
            if car.xcor()<-280:
                car.goto(280,random.choice(LANES))
    def increase_speed(self):
        self.speed +=10




