from turtle import Turtle
import snake
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()  #把要繼承的attribute寫進去，如果新定義的，寫在上一行的__init__中編進去；再在super下行開始定義
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed(0)
        self.move()

    def move(self):
        # size = 10
        # self.x_size = [self.xcor()-size,self.xcor()+size]
        # self.y_size = [self.ycor()-size,self.ycor()+size]
        # print(self.x_size,self.y_size)
        # condition_1 = self.x_size[0] < snake.dots_in_snake[0].xcor() < self.x_size[1]
        # condition_2 = self.y_size[0] < snake.dots_in_snake[0].ycor() < self.y_size[1]
        # if condition_1 and condition_2:
        #     self.goto(random.randrange(-280,280),random.randrange(-280,280))
        self.goto(random.randrange(-260,260),random.randrange(-260,260))






