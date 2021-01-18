
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        # we want to hidden the turtle itself
        self.hideturtle()
        # create the attribute for this score class:
        self.l_score = 0
        self.r_score = 0
        # we call update scoreboard when we first initialize it:
        self.update_scoreboard()

    def update_scoreboard(self):
        # our scoreboard is going to track how our left and right paddles are doing
        # for the left paddle:
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # for the right paddle:
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # to increase the point of the left paddle
    def l_point(self):
        self.l_score += 1
        # also we update our scoreboard when we add a point
        # before we update our scoreboard we need to clean the previous result of the scoreboard
        self.clear()
        self.update_scoreboard()

    # to increase the point of the right paddle
    def r_point(self):
        self.r_score += 1
        # also we update our scoreboard when we add a point
        self.clear()
        self.update_scoreboard()
