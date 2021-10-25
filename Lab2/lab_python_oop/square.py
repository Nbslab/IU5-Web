from lab_python_oop.figure import Figure
from lab_python_oop.colour import FigureColour


class Square(Figure):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, side):
        self.side = side
        self.colour = FigureColour()
        self.colour.colourproperty = color

    def square(self):
        return self.side ** 2

    def __repr__(self):
        return f'{Square.get_type()} {self.colour.colourproperty} цвета со стороной {self.side} и площадью {self.square()}.'
