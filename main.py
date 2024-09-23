import board
from draw_utils import *
import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
grid = board.OrthoGrid(3, 3, 200)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(White)
    grid.draw(screen)
    pg.display.flip()

pg.quit()
