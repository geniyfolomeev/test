from figure_interface import AbstractFigure
from turtle import Turtle


class Triangle(AbstractFigure):
    def __init__(
            self,
            side_length: float,
            x=0,
            y=0,
    ):
        super().__init__(x, y)
        self.side_length = side_length

    def draw(self, turtle: Turtle):
        print(f"Drawing {self.color} Triangle:{turtle.pos()} with side length {self.side_length}")
        for _ in range(3):
            turtle.forward(self.side_length)
            turtle.left(120)
