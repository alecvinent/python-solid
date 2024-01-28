from ..shape import Shape


class SquareShape(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return pow(self.side, 2)
