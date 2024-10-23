from enum import Enum


class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    magenta = (255, 0, 255)


player_colors = [
    Color.red,
    Color.green,
    Color.blue,
    Color.yellow,
    Color.black,
    Color.white,
]


class Shape(Enum):
    square = "square"
    circle = "circle"
