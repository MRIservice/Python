from turtle import Turtle


HEIGHT = 800
WIDTH = 1200


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("orange")
        self.shapesize(stretch_wid=WIDTH * .004,
                       stretch_len=HEIGHT * .0004, outline=None)
        self.goto(location)

        
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
