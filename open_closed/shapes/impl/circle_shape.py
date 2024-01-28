from math import pi

from ..shape import Shape


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * pow(self.radius, 2)
