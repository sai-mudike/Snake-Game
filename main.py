from turtle import Screen
from snake import Snake
import time


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title('My segement Game')
screen.tracer(0)
screen.listen()



snake=Snake()

screen.onkey(snake.up,key="Up")
screen.onkey(snake.down,key="Down")
screen.onkey(snake.right,key="Right")
screen.onkey(snake.left,key="Left")




is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
        
        




screen.exitonclick()