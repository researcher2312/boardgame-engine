import board
import player
import pawn
from draw_utils import Color, Shape
import pygame as pg

pg.init()
player_manager = player.PlayerManager(2)
grid = board.OrthoGrid(3, 3, 200)
screen = pg.display.set_mode((grid.width, grid.height))
test_pawn = pawn.Pawn(Shape.circle, 100, 100, 60)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(Color.white)
    grid.draw(screen)
    test_pawn.draw(screen)
    pg.display.flip()

pg.quit()
