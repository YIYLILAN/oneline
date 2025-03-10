import pygame
from GRID import Grid

class Player:

    def __init__(self, grid, start_pos):
        
        self.grid = grid  # The grid object(different game board)
        self.row, self.col = start_pos 
        self.route = set()  # Stores visited cells
        self.route.add((self.row, self.col))  # Mark start position as visited on the route

    def move(self, direction):
        
        new_row, new_col = self.row, self.col

        if direction == "up":
            new_row -= 1
        elif direction == "down":
            new_row += 1
        elif direction == "left":
            new_col -= 1
        elif direction == "right":
            new_col += 1

        # move within bounds of the board and are not in the route/track
        if self.grid.is_valid_move(new_row, new_col, self.route): #is_valid_move() from Grid
            self.row, self.col = new_row, new_col
            self.route.add((self.row, self.col)) 



