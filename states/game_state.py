import pygame
from states.base_state import BaseState
from config.LEVELS import LEVELS, find_tile, count_walkable

from Modules.BUTTON import Buttons
from config.setting import reverse_button, reset_button

class MazeGameState(BaseState):
    def __init__(self, screen, game_manager, level):
        super().__init__(screen)
        self.game_manager = game_manager
        self.level = level
        self.maze = LEVELS[level]
        self.start = find_tile(self.maze, 2)
        self.end = find_tile(self.maze, 3)
        self.player_pos = self.start
        self.visited = {self.player_pos}
        self.path_stack = [self.player_pos]
        self.walkable_tiles = count_walkable(self.maze)
        self.button_height = 80

        # Buttons
        self.reverse_button = Buttons(100, self.screen.get_height() - 40, reverse_button)
        self.reset_button = Buttons(300, self.screen.get_height() - 40, reset_button)

    def enter(self):
        print(f"Entered MazeGameState for Level {self.level}")

    def move_player(self, dx, dy):
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        new_pos = (new_x, new_y)

        if 0 <= new_x < len(self.maze) and 0 <= new_y < len(self.maze[0]):
            if self.maze[new_x][new_y] != 1 and new_pos not in self.visited:
                self.player_pos = new_pos
                self.visited.add(new_pos)
                self.path_stack.append(new_pos)
            elif new_pos in self.visited:
                print("Grid already visited")

        if self.player_pos == self.end:
            if len(self.visited) == self.walkable_tiles:
                print("CONGRATS! You passed all tiles.")
                self.game_manager.unlock_next_level(self.level)
            else:
                print("You reached the end but missed some tiles.")

    def reverse_move(self):
        if len(self.path_stack) > 1:
            self.path_stack.pop()
            self.player_pos = self.path_stack[-1]
            self.visited = set(self.path_stack)

    def reset_game(self):
        self.player_pos = self.start
        self.visited = {self.player_pos}
        self.path_stack = [self.player_pos]

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_manager.pop_state()
                elif event.key == pygame.K_UP:
                    self.move_player(-1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move_player(1, 0)
                elif event.key == pygame.K_LEFT:
                    self.move_player(0, -1)
                elif event.key == pygame.K_RIGHT:
                    self.move_player(0, 1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.reverse_button.press_key():
                    self.reverse_move()
                elif self.reset_button.press_key():
                    self.reset_game()

    def render(self):
        self.screen.fill((0, 0, 0))  # 背景改为黑色

        rows, cols = len(self.maze), len(self.maze[0])
        usable_height = self.screen.get_height() - self.button_height
        cell_size = min(self.screen.get_width() // cols, usable_height // rows)

        offset_y = (usable_height - rows * cell_size) // 2

        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                x = j * cell_size
                y = offset_y + i * cell_size
                rect = pygame.Rect(x, y, cell_size, cell_size)

                pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)  # 白色线框格子

                if cell == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)
                elif cell == 2:
                    pygame.draw.rect(self.screen, (175, 255, 175), rect)
                elif cell == 3:
                    pygame.draw.rect(self.screen, (175, 176, 255), rect)

        for x, y in self.visited:
            pygame.draw.circle(self.screen, (200, 195, 230),
                (y * cell_size + cell_size // 2, offset_y + x * cell_size + cell_size // 2), 6)

        px, py = self.player_pos
        pygame.draw.circle(self.screen, (255, 206, 227),
            (py * cell_size + cell_size // 2, offset_y + px * cell_size + cell_size // 2), cell_size // 3)

        self.reverse_button.draw(self.screen)
        self.reset_button.draw(self.screen)

        pygame.display.update()
