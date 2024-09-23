from draw_utils import *
import pygame as pg

class OrthoGrid:
    def __init__(self, size_x, size_y, cell_size):
        self.size_x = size_x
        self.size_y = size_y
        self.cell_size = cell_size
        self.grid = [[0]*size_x for i in range(size_y)]

    def draw(self, screen):
        width = self.size_x * self.cell_size
        height = self.size_y * self.cell_size
        pg.draw.rect(screen, Black,(0, 0, width, height), 5)
        for i in range(self.size_x):
            line_x = i * self.cell_size
            pg.draw.line(screen, Black, (line_x, 0), (line_x, height), 5)
        for i in range(self.size_y):
            line_y = i * self.cell_size
            pg.draw.line(screen, Black, (0, line_y), (width, line_y), 5)
