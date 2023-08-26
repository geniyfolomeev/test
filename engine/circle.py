from figure_interface import AbstractFigure
from turtle import Turtle


class Circle(AbstractFigure):
    def __init__(
            self,
            radius: float,
            x=0,
            y=0,
    ):
        super().__init__(x, y)
        self.radius = radius

    def draw(self, turtle: Turtle):
        print(f"Drawing {self.color} Circle:{turtle.pos()} with radius {self.radius}")
        turtle.circle(self.radius)
