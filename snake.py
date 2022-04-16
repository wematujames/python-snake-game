from turtle import Turtle, Screen

SNAKE_HIEGHT = 0.5
SNAKE_WIDTH = 0.5

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake: 
    def __init__(self):
        self.create_snake()
        self.head = self.turtles[0]
        
        
    # new snake
    def create_snake(self):
        self.turtles = []
        for i in range(3):
            turtle = Turtle(shape="square")
            turtle.penup()
            turtle.shapesize(SNAKE_HIEGHT, SNAKE_WIDTH)
            turtle.color("white")
            turtle.goto(i * -9,0)
            self.turtles.append(turtle)
        
    # grow turtle 
    def grow (self):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.shapesize(SNAKE_HIEGHT, SNAKE_WIDTH)
        turtle.color("white")
        turtle.goto(self.turtles[-1].xcor(), self.turtles[-1].ycor())
        self.turtles.append(turtle)
        
    # movement
    def move(self):
            for turtle in range(len(self.turtles) - 1, 0 , -1):
                self.turtles[turtle].goto(self.turtles[turtle - 1].xcor(), self.turtles[turtle - 1].ycor())
            self.head.forward(10)
            
        
    def up (self): 
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
        
    def left (self): 
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
        
    def right (self): 
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
        
    def down (self): 
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        

