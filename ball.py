
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # creating the attribute:
        self.x_move = 10
        self.y_move = 10
        # set the initial speed of the ball:
        self.sleep_time = 0.1


    def move(self):
        # our ball is going to move from 0,0 position to increasing position:
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def ball_bounce_y(self):
        # we need to reverse the direction when the ball bounces from the wall
        # for this we change the position of y access for opposite position
        self.y_move *= -1

    def ball_bounce_x(self):
        # we reverse the x access moving when the ball bounces the paddle
        self.x_move *= -1
        # every single time our ball bounces in x access it means it has been touched by the paddle, we increase the speed
        # of the ball in the way to reduce the sleep time of the screen
        self.sleep_time *= 0.9


    # when the paddle miss the ball we put it in an initial position and we want
    # the ball to go to inverse direction
    def reset_position(self):
        self.goto(0, 0)
        # when the game starts from the beginning we need to set the screen time sleep (ball speed) at the beginning
        self.sleep_time = 0.1
        self.ball_bounce_x()




    # def update_speed(self):
    #     self.speed_ball += 10
    #     self.increase_speed()





