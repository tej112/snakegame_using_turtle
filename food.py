from turtle import Turtle
from random import randint


class Food(Turtle):
    """Here Food object is created using Turtle Object inheritance
        This food object is generated at a random position on the screen."""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(randint(-280,280),randint(-280,280))

    