from draw_utils import *
import pygame as pg

class OrthoGrid:
    def __init__(self, size_x, size_y, cell_size):
        self.size_x = size_x
        self.size_y = size_y
        self.cell_size = cell_size
        self.width = size_x * cell_size
        self.height = size_y * cell_size
        self.grid = [[0]*size_x for _ in range(size_y)]

    def draw(self, screen):
        pg.draw.rect(screen, Color.black,(0, 0, self.width, self.height), 5)
        for i in range(self.size_x):
            line_x = i * self.cell_size
            pg.draw.line(screen, Color.black, (line_x, 0), (line_x, self.height), 5)
        for i in range(self.size_y):
            line_y = i * self.cell_size
            pg.draw.line(screen, Color.black, (0, line_y), (self.width, line_y), 5)
