from turtle import Turtle

STARTING_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segement_parts=[]
        self.create_snake()
        self.head=self.segement_parts[0]
    
    def create_snake(self):
        for i in range(3):
            segement=Turtle('square')
            segement.color("white")
            segement.penup()
            self.segement_parts.append(segement)
            segement.goto(STARTING_POS[i])
            
        

    def move(self):
        for seg in range(len(self.segement_parts)-1,0,-1):
            new_x=self.segement_parts[seg-1].xcor()
            new_y=self.segement_parts[seg-1].ycor()
            self.segement_parts[seg].goto((new_x,new_y))
        self.head.forward(MOVE_DISTANCE)

    def up(self):

        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)