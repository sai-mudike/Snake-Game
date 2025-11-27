from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,280)
        self.color("white")
        self.write(arg=f"Score: {self.score}",align="center",font=("Arial",10,"normal"))


    def add_one_point(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score: {self.score}",align="center",font=("Arial",10,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER",align="center",font=("Arial",24,"normal"))