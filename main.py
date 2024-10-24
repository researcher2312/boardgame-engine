import board
import player
import pawn
from draw_utils import Color, Shape
import pygame as pg


pg.init()
player_manager = player.PlayerManager(2)
grid = board.OrthoGrid(3, 3, 200)
screen = pg.display.set_mode((grid.width, grid.height))
pawn_1 = pawn.Pawn(Shape.circle, 100, 100, 60)
pawn_2 = pawn.Pawn(Shape.circle, 100, 200, 60)
pawns = [pawn_1, pawn_2]

    
running = True
selected = None
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, pawn in enumerate(pawns):
                    # Pythagoras a^2 + b^2 = c^2
                    dx = pawn.x - event.pos[0] # a
                    dy = pawn.y - event.pos[1] # b
                    distance_square = dx**2 + dy**2 # c^2

                    if distance_square <= pawn.w**2: # c^2 <= radius^2
                        selected = i
                        selected_offset_x = pawn.x - event.pos[0]
                        selected_offset_y = pawn.y - event.pos[1]
            
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                selected = None
            
        elif event.type == pg.MOUSEMOTION:
            if selected is not None: # selected can be `0` so `is not None` is required
                # move object
                pawns[selected].x = event.pos[0] + selected_offset_x
                pawns[selected].y = event.pos[1] + selected_offset_y
    
    screen.fill(Color.white)
    grid.draw(screen)
    [x.draw(screen) for x in pawns]
    pg.display.flip()

pg.quit()
