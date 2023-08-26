from turtle import (
    Screen,
    Turtle,
)
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from figure_interface import AbstractFigure
from colors import Colors


class Engine2D:
    def __init__(self):
        self.canvas: list[AbstractFigure] = []
        self.screen = Screen()
        self.turtle = Turtle()
        self.color = Colors.BLACK

    def add_figure_to_canvas(self, figure: AbstractFigure):
        figure.set_color(self.color)
        self.canvas.append(figure)

    def draw(self):
        for figure in self.canvas:
            self.turtle.color(figure.color)
            self.turtle.penup()
            self.turtle.goto(figure.x, figure.y)
            self.turtle.pendown()
            figure.draw(self.turtle)
        self.canvas.clear()
        self.turtle.clear()

    def change_color(self, color: Colors):
        self.color = color


if __name__ == '__main__':
    engine = Engine2D()

    circle = Circle(radius=50, x=5, y=30)
    triangle = Triangle(side_length=100, x=-40, y=-10)
    rectangle = Rectangle(length=70, height=40)

    engine.add_figure_to_canvas(circle)

    engine.change_color(Colors.BLUE)
    engine.add_figure_to_canvas(triangle)

    engine.change_color(Colors.RED)
    engine.add_figure_to_canvas(rectangle)

    engine.draw()

    engine.change_color(Colors.PURPLE)
    engine.add_figure_to_canvas(triangle)
    engine.draw()

    engine.screen.exitonclick()
