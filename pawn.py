import pygame as pg
from draw_utils import Shape, Color


class Pawn:
    def __init__(self, shape: Shape, x: int = 0, y: int = 0, w: int = 0, h: int = 0):
        self.shape = shape
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, screen):
        if self.shape == Shape.square:
            pg.draw.rect(screen, Color.black, (self.x, self.y, self.w, self.h), 0)
        else:
            pg.draw.circle(screen, Color.black, (self.x, self.y), self.w, 0)
