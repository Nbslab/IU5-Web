from lab_python_oop.figure import Figure
from lab_python_oop.colour import FigureColour
import math


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, colour, radius):
        self.radius = radius
        self.color = FigureColour()
        self.color.colourproperty = colour

    def square(self):
        return round(math.pi * (self.radius ** 2), 2)

    def __repr__(self):
        return f'{Circle.get_figure_type()} {self.color.colourproperty} цвета радиуса {self.radius} и площадью {self.square()}.'
