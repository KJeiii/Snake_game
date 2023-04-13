from distutils.command.install_egg_info import safe_name
from turtle import Turtle, Screen, tracer, update
import snake
import food
import score
import time

#設定背景顏色、大小、標題
t = Turtle()
scr = Screen()
scr.setup(width = 600, height = 600)
scr.bgcolor('black')
scr.title('My snake game.')
    
#設定蛇的動作畫面，叫出snake、food
scr.tracer(0)
Snake = snake.Snake(10,'square')
Food = food.Food()
Score = score.Scoreboard()


#設定遊戲按鍵
scr.listen()
scr.onkey(fun = Snake.up_move, key = "Up")
scr.onkey(fun = Snake.down_move, key = "Down")
scr.onkey(fun = Snake.left_move, key = "Left")
scr.onkey(fun = Snake.right_move, key = "Right")   

#設定snake、food動作
is_snake_surive = True
while is_snake_surive:
    time.sleep(0.09)
    Snake.move()

    #gameover condition-wall collision
    condition_1 = abs(snake.dots_in_snake[0].xcor()) > 280
    condition_2 = abs(snake.dots_in_snake[0].ycor()) > 280 
    if condition_1 or condition_2:
        Score.reset()
        Snake.reborn()
        # is_snake_surive = False
        # score.GameOver()

    #gameover condtion-tail collision
    for dot in snake.dots_in_snake[1:]:
        if snake.dots_in_snake[0].distance(dot) < 10:
            Score.reset()
            Snake.reborn()
            # is_snake_surive = False
            # score.GameOver()

    #food_refresh、scoreboard
    if snake.dots_in_snake[0].distance(Food) < 15:
        Food.move()
        Score.getscore()
        Snake.grow()

    scr.update()

scr.exitonclick()








