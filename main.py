import pygame as pg
import os
from numpy import array
from board import Board
from board import Game

pg.init()

screen = pg.display.set_mode((1280, 720))
board = Board(screen)
game = Game(screen)
squares = board.draw_board()
rows = []
for row in range(8):
    start_index = row * 8
    end_index = start_index + 8
    rows.append(squares[start_index:end_index])

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            for row in range(8):
                for col in range(8):
                    x, y, width, height = rows[row][col]
                    mouse_x, mouse_y = mouse_pos
                    if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
                        game.highlight_piece()
                        break

    screen.fill((255, 0, 255))
    board.draw_board()
    game.draw_pieces()
    pg.display.flip()

pg.quit()
