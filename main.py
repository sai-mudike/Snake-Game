from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title('My segement Game')
screen.tracer(0)
screen.listen()



snake=Snake()
food=Food()
score=ScoreBoard()

screen.onkey(snake.up,key="Up")
screen.onkey(snake.down,key="Down")
screen.onkey(snake.right,key="Right")
screen.onkey(snake.left,key="Left")




is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # collision with food

    if snake.head.distance(food)<15:
        food.refresh()
        score.add_one_point()
    
    # detect collision with wall

    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        
        is_game_on=False
        score.game_over()
        
    
        
        




screen.exitonclick()