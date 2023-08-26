from figure_interface import AbstractFigure
from turtle import Turtle


class Rectangle(AbstractFigure):
    def __init__(
            self,
            length: float,
            height: float,
            x=0,
            y=0,
    ):
        super().__init__(x, y)
        self.length = length
        self.height = height

    def draw(self, turtle: Turtle):
        print(f"Drawing {self.color} Rectangle:{turtle.pos()} with length {self.length} and height {self.height}")
        for _ in range(2):
            turtle.forward(self.length)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
