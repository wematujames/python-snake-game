from turtle import Turtle

TEXT_ALIGMENT = "center"
FONT = ("Courier", 16, "normal")
SCOREBOARDX = 0
SCOREBOARDY = 260


class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.create_scoreboard()
        self.update_score()
        
    #init scoreboard
    def create_scoreboard (self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(SCOREBOARDX, SCOREBOARDY)
    
    # On game over, display game over message
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=TEXT_ALIGMENT, font=FONT)
    
    #update score
    def update_score(self):
       self.clear()
       self.write(f"Score: {self.score} High Score: {self.high_score}", align=TEXT_ALIGMENT, font=FONT)    
    
    # Increase score
    def add_score (self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()
        