from .rectangle_shape import RectangleShape


class SquareShape(RectangleShape):
    def __init__(self, side):
        super().__init__(width=side, height=side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ('width', 'height'):
            self.__dict__['width'] = value
            self.__dict__['height'] = value
