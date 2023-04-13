from turtle import Turtle
turtle = Turtle()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,270)
        with open('./high_score.txt',mode='r') as file:
            self.high_score = int(file.read())
        self.write(f'Score : {self.score}；High Score ： {self.high_score}',align='Center',font=('Aria',20,'normal'))

    def getscore(self):
        self.clear()
        self.score += 1
        self.write(f'Score : {self.score}；High Score ： {self.high_score}',align='Center',font=('Aria',20,'normal'))

    def reset(self):
        if self.score > self.high_score : 
            self.high_score = self.score
            with open('Udemy-100Days/Turtle/Snake game/high_score.txt',mode='w') as file:
                file.write(str(self.high_score))
        self.clear()
        self.score = 0
        self.write(f'Score : {self.score}；High Score ： {self.high_score}',align='Center',font=('Aria',20,'normal'))



  
class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.home()
        self.write('Game Over.',align='center',font=('Arial',20,'normal'))
