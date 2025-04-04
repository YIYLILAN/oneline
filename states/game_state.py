import pygame
from states.base_state import BaseState

class MazeGameState(BaseState):
    def __init__(self, screen, game):
        super().__init__(screen)
        self.game = game
        self.player_pos = (0, 3)  # Start position

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to return to menu
                    self.game.change_state(self.game.menu)


    def render(self):
        self.screen.fill((255, 255, 250))
        font = pygame.font.SysFont("arial", 20)
        text = font.render("Maze Game - Press ESC to Menu", True, (0, 0, 0))
        self.screen.blit(text, (50, 250))
        pygame.display.update()
