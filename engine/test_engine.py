import pytest
from pytest import CaptureFixture
from engine_2d import (
    Engine2D,
    Circle,
    Colors,
)


@pytest.fixture()
def engine() -> Engine2D:
    return Engine2D()


@pytest.fixture()
def circle():
    return Circle(radius=10, x=10, y=-10)


def test_add_to_canvas(
        engine: Engine2D,
        circle: Circle,
):
    engine.add_figure_to_canvas(circle)

    assert circle in engine.canvas


def test_figure_color(
        engine: Engine2D,
        circle: Circle,
        color=Colors.RED
):
    engine.change_color(color)
    engine.add_figure_to_canvas(circle)

    assert circle.color == color


def test_clear_canvas(
        engine: Engine2D,
        circle: Circle,
):
    engine.add_figure_to_canvas(circle)
    engine.draw()

    assert len(engine.canvas) == 0


def test_log(
        engine: Engine2D,
        circle: Circle,
        capsys: CaptureFixture,
        color=Colors.PURPLE
):
    engine.change_color(color)
    engine.add_figure_to_canvas(circle)
    engine.draw()

    log = capsys.readouterr().out.replace('\n', '')
    assert log == f'Drawing {color} Circle:{engine.turtle.pos()} with radius {circle.radius}'
