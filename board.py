import pygame as pg
import os
pg.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Board:
    def __init__(self, screen, start_x=300, start_y=10, square_size=75):
        self.screen = screen
        self.start_x = start_x
        self.start_y = start_y
        self.square_size = square_size
        self.board = []
    
    def draw_square(self, x, y, color):
        square = pg.Rect(x, y, self.square_size, self.square_size)
        pg.draw.rect(self.screen, color, square)
        return (x, y, self.square_size, self.square_size)
    
    def draw_row(self, y, row_index):
        squares = []
        for i in range(8):
            color = (238, 238, 210) if (i + row_index) % 2 == 0 else (118, 150, 86)
            x = self.start_x + i * self.square_size
            coords = self.draw_square(x, y, color)
            squares.append(coords)
        return squares

    def draw_board(self):
        y = self.start_y
        for row_index in range(8):
            self.board.extend(self.draw_row(y, row_index))
            y += self.square_size
        return self.board

    


import pygame as pg
import os

pg.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Board:
    def __init__(self, screen, start_x=300, start_y=10, square_size=75):
        self.screen = screen
        self.start_x = start_x
        self.start_y = start_y
        self.square_size = square_size
        self.board = []
    
    def draw_square(self, x, y, color):
        square = pg.Rect(x, y, self.square_size, self.square_size)
        pg.draw.rect(self.screen, color, square)
        return (x, y, self.square_size, self.square_size)
    
    def draw_row(self, y, row_index):
        squares = []
        for i in range(8):
            color = (238, 238, 210) if (i + row_index) % 2 == 0 else (118, 150, 86)
            x = self.start_x + i * self.square_size
            coords = self.draw_square(x, y, color)
            squares.append(coords)
        return squares

    def draw_board(self):
        y = self.start_y
        for row_index in range(8):
            self.board.extend(self.draw_row(y, row_index))
            y += self.square_size
        return self.board

class Game:
    def __init__(self, screen):
        self.chessboard = [
            ["black-rook", "black-knight", "black-bishop", "black-queen", "black-king", "black-bishop", "black-knight", "black-rook"],
            ["black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn"],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["..", "..", "..", "..", "..", "..", "..", ".."],
            ["white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn"],
            ["white-rook", "white-knight", "white-bishop", "white-queen", "white-king", "white-bishop", "white-knight", "white-rook"]
        ]
        self.currentturn = 'w'  # white to move
        self.ischeckmate = False
        self.images = {}
        self.screen = screen
        self.piece_load()  # Load the pieces during initialization

    def piece_load(self):
        image_folder = "images"
        piece_types = ("black-bishop", "black-king", "black-knight", "black-pawn", "black-queen", "black-rook", 
                       "white-bishop", "white-king", "white-knight", "white-pawn", "white-queen", "white-rook")
        for piece in piece_types:
            image_path = os.path.join(image_folder, f"{piece}.png")
            if os.path.exists(image_path):
                self.images[piece] = pg.transform.scale(pg.image.load(image_path), (75, 75))

    def draw_pieces(self):
        for row_i, row in enumerate(self.chessboard):
            for col_i, piece in enumerate(row):
                if piece != ".." and piece in self.images:
                    x = 75 * col_i + 300
                    y = 75 * row_i + 10
                    piece_image = self.images[piece]
                    self.screen.blit(piece_image, (x, y))
    
    def highlight_piece(self):
        for row_i, row in enumerate(self.chessboard):
            for col_i, piece in enumerate(row):
                if piece != ".." and piece in self.images:
                    print(f"{row_i}, {col_i} {piece}")