from turtle import Turtle
import random

class Food (Turtle) : 
    def __init__(self):
        super().__init__()
        self.food = Turtle()
        self.food.penup()
        self.food.shape("circle")
        self.food.shapesize(0.5, 0.5)
        self.food.color("red")
        self.refresh()
        
    def refresh (self):
        self.food.goto(random.randint(-280, 280),random.randint(-280, 280))