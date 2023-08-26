from abc import ABC, abstractmethod
from turtle import Turtle
from colors import Colors


class AbstractFigure(ABC):
    def __init__(
            self,
            x: int,
            y: int,
    ):
        self.x = x
        self.y = y
        self.color = Colors.BLACK

    @abstractmethod
    def draw(self, turtle: Turtle):
        pass

    def set_color(self, color):
        self.color = color
