from turtle import Turtle


# CREATING A PADDLE CLASS
class Paddle(Turtle):
    # the paddle class needs to take an input when it is initialized, we need a position to pass there
    # the position will determine where the paddle needs to go to
    def __init__(self, position):
        super().__init__()
        # now we are inside the paddle class which is the same as turtle class with some added extras
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # CREATING A GO_UP FUNCTION FOR PADDLE
    def go_up(self):
        # we are changing y position, it will be the current ycor position, but its going to go up by 20px
        # We use self.ycor() so that it's referring to the object that is created from this class
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # CREATING A GO_DOWN FUNCTION FOR PADDLE
    def go_down(self):
        # we are changing y position, it will be the current ycor position, but its going to go down by 20px
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




