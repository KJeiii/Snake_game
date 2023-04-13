from turtle import Turtle
t = Turtle()
#設定蛇的初始狀態
# t.shapesize(stretch_len=5,stretch_wid=1)  > 如果用這個方式製造蛇，就不能判斷是否會自撞
dots_in_snake = []  #dot object
# dots_pos_in_snake = []
snake_body = []  #dot position, tutple (xcor,ycor)


class Snake(): 
    def __init__(self,init_len,shape):
        self.init_len = init_len
        self.shape = shape
        x = 0
        for n in range(self.init_len):
            a = Turtle(shape = self.shape)
            a.color('white')  #會一起改掉pencolor、fillcolor
            a.penup()
            a.goto(x,0)
            dots_in_snake.append(a)
            snake_body.append(n)
            x = a.xcor()-20

    def move(self):
        # dots_x_in_snake = [dots_in_snake[n].xcor() for n in range(self.init_len)]
        # dots_y_in_snake = [dots_in_snake[n].ycor() for n in range(self.init_len)]
        # for n in range(0,self.init_len):
        #     a = tuple([dots_x_in_snake[n],dots_y_in_snake[n]])
        #     dots_pos_in_snake.append(a)
        #for n in range(1,init_len):
        #a = tuple([dot_x_in_snake[n],dot_y_in_snake[n]])

        step = 20
        for n in range(len(dots_in_snake)-1,0,-1):
            new_x = dots_in_snake[n-1].xcor()
            new_y = dots_in_snake[n-1].ycor()
            dots_in_snake[n].goto(new_x,new_y)
            snake_body[abs(n-len(dots_in_snake)+1)] = (new_x,new_y)

            # dot_in_snake[n].goto(dot_pos_in_snake[n-1]) 

        dots_in_snake[0].forward(step)
        # for n in range(0,init_len-1):
        # dot_pos_in_snake[n] = dot_in_snake[n].pos()

    def grow(self):
        new_dot = Turtle(shape = self.shape)
        new_dot.color('white')  
        new_dot.penup()
        last_dot_num = len(dots_in_snake)-1
        last_dot_pos = snake_body[last_dot_num-1]
        new_dot.goto(last_dot_pos)
        snake_body.append(new_dot.pos())
        dots_in_snake.append(new_dot)
    
    def reborn(self):
        for dot in dots_in_snake:
            dot.hideturtle()
        dots_in_snake.clear()
        snake_body.clear()
        x = 0
        for n in range(self.init_len):
            a = Turtle(shape = self.shape)
            a.color('white')  #會一起改掉pencolor、fillcolor
            a.penup()
            a.goto(x,0)
            dots_in_snake.append(a)
            snake_body.append(n)
            x = a.xcor()-20
    

        #設定遊戲動作
    def up_move(self):
        if dots_in_snake[0].heading() != 270:
            dots_in_snake[0].setheading(90)

    def down_move(self):
        if dots_in_snake[0].heading() != 90:
            dots_in_snake[0].setheading(270)

    def left_move(self):
        if dots_in_snake[0].heading() != 0:
            dots_in_snake[0].setheading(180)

    def right_move(self):
        if dots_in_snake[0].heading() != 180:
           dots_in_snake[0].setheading(0)

