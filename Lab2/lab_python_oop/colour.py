class FigureColour:
    def __init__(self):
        self._colour = None

    @property
    def colourproperty(self):
        return self._colour

    @colourproperty.setter
    def colourproperty(self, value):
        self._colour = value
