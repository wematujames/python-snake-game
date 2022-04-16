from turtle import Screen, Turtle
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenxia Annex")
screen.tracer(0)



#create snake
wematu = Snake()
food = Food()
scoreboard = Scoreboard()

# Event listeners for snake movement
screen.onkey(wematu.up, "Up") 
screen.onkey(wematu.down, "Down") 
screen.onkey(wematu.left, "Left")
screen.onkey(wematu.right, "Right") 
screen.listen()

# Main game loop
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    wematu.move()

    # Check for collision with food
    if wematu.head.distance(food.food) < 10:
        food.refresh()
        wematu.grow()
        scoreboard.add_score()
        
    # Check for collision with wall
    if wematu.head.xcor() < -290 or wematu.head.xcor() > 290 or wematu.head.ycor() < -290 or wematu.head.ycor() > 290:
        game_on = False
        scoreboard.game_over()
        
    # check for collosion with tail
    for part in wematu.turtles[1:]:
        if wematu.head.distance(part) < 0.1:
            game_on = False
            scoreboard.game_over()
    
    


        
        

















screen.exitonclick()

# while game_on:
#     for turtle in turtles:
#         turtle.forward(10)
#         if turtle.xcor() > 300:
#             turtle.right(90)
#         elif turtle.xcor() < -300:
#             turtle.left(90)
#         elif turtle.ycor() > 300:
#             turtle.right(90)
#         elif turtle.ycor() < -300:
#             turtle.left(90)
#         else:
#             pass