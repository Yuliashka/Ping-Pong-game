
from turtle import Turtle

class Center(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.hideturtle()
        self.penup()
        self.goto(0, -300)
        self.left(90)
        while self.ycor() < 310:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)






