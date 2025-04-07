import pygame
from states.base_state import BaseState

class MazeGameState(BaseState):
    def __init__(self, screen, game, level):
        super().__init__(screen)
        self.game = game
        self.level = level
        self.maze_layout = self.load_maze(level)
        self.player_pos = (0, 0)


    def set_level(self, level):
        self.level = level
        self.player_pos = (0, 3)  # Start pos, can be different per level how would i change?
        self.visited = {self.player_pos}
        self.load_maze(level)

    def load_maze(self, level):
        # Define different mazes here based on level
        if level == 1:
            self.maze = [
                [0, 0, 0, 2],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [3, 0, 0, 0]
            ]
        elif level == 2:
            self.maze = [  # harder maze
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 2, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [3, 0, 0, 0, 0, 0]
            ]
        # ... up to level 5

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.change_state(self.game.menu)

    def render(self):
        self.screen.fill((255, 255, 250))
        font = pygame.font.SysFont("arial", 20)
        text = font.render("Maze Game - Press ESC to Menu", True, (0, 0, 0))
        self.screen.blit(text, (50, 250))
        pygame.display.update()

