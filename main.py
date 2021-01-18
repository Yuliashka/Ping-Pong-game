
from turtle import Screen
from paddle import Paddle
from ball import Ball
# we need to import a time module to move our ball not so fast
import time
from scoreboard import Scoreboard
from center import Center

# CREATING A SCREEN
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong!")
# to control the animation of the screen, we use tracer method and put 0 to off the animation
screen.tracer(0)
# when we turn off the animation we have to manually update the screen and refresh it every single time

# CREATING CENTER OBJECT
center = Center()


# CREATING PADDLE OBJECTS:
# we have different positions, we pass a position to our paddles
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

# CREATING BALL OBJECT
ball = Ball()

# CREATING A SCOREBOARD OBJECT
scoreboard = Scoreboard()

# CREATING A SCREEN CONTROL
screen.listen()
# to control right paddle we use keys:
screen.onkey(key="Up", fun=paddle_right.go_up)
screen.onkey(key="Down", fun=paddle_right.go_down)
# to control left paddle we use keys:
screen.onkey(key="w", fun=paddle_left.go_up)
screen.onkey(key="s", fun=paddle_left.go_down)

# TO UPDATE OUR SCREEN AUTOMATICALLY EVERY TIME WE CREATE A WHILE LOOP
game_is_on = True
while game_is_on:
    # we need a time module to make our while loop to sleep for a little bit in between each of updates
    # this time sleeping makes effect also at the ball's speed. To make it move faster we need to make the time shorter
    time.sleep(ball.sleep_time)
    screen.update()
    # using a move() method for our ball to make it move from the up and down walls
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()

    # detect ball collision with the paddle
    # when we use method distance it measure only the distance between 2 centers of objects
    # so if our ball makes the collision in the end of paddle we must remember that the
    # paddle has length more that 50 px
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.ball_bounce_x()

    # detect when right paddle miss the ball
    # the width of the screen is 800 (400 in two directions), the paddle is placed at x access 350
    # so if the ball passes 380 x access the right paddle has missed the ball and we want to reset ball's position
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # to detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()
