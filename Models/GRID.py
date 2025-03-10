import pygame


class Grid:
    def __init__(self, rows, cols, cell_size, start_pos, finish_pos):
        
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.start_pos = start_pos
        self.finish_pos = finish_pos

    def is_valid_move(self, row, col, route):
        return (0 <= row < self.rows and 0 <= col < self.cols) and (row, col) not in route
    