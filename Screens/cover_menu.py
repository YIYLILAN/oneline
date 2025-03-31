import pygame
from base_state import BaseState

class MenuState(BaseState):
    def __init__(self, screen, game):
        super().__init__(screen, game)
        self.font = pygame.font.SysFont("arial", 50)
        self.start_button = pygame.Rect(125, 250, 150, 50)
        self.quit_button = pygame.Rect(125, 350, 150, 50)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(event.pos):
                    self.game.change_state(self.game.maze_game)
                elif self.quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

    def update(self):
        pass

    def render(self):
        self.screen.fill((231, 245, 255))
        title_text = self.font.render("ONE_LINE", True, (0, 0, 0))
        self.screen.blit(title_text, (100, 100))

        pygame.draw.rect(self.screen, (91, 135, 227), self.start_button)
        pygame.draw.rect(self.screen, (91, 135, 227), self.quit_button)

        text_start = self.font.render("Start", True, (255, 255, 255))
        text_quit = self.font.render("Quit", True, (255, 255, 255))

        self.screen.blit(text_start, (150, 260))
        self.screen.blit(text_quit, (150, 360))

        pygame.display.update()
