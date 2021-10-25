from lab_python_oop.figure import Figure
from lab_python_oop.colour import FigureColour


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, colour, width, height):
        self.width = width
        self.height = height
        self.colour = FigureColour()
        self.colour.colourproperty = colour

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return f'{Rectangle.get_type()} {self.colour.colourproperty} цвета шириной {self.width} и высотой {self.height} площадью {self.square()}.'
