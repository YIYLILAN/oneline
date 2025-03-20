import pygame
from base_state import BaseState
from config.setting import HEIGHT,WIDTH, WHITE, BLACK, font

class MenuState(BaseState):
    def __init__(self, screen, game):
        super().__init__(screen)
        self.game = game #add game to allow state change.
        self.start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
        self.level_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)

    def handle_events(self, events):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and click[0] == 1:
                if self.start_button.collidepoint(mouse):
                    self.game.change_state("game") # change state to game
                elif self.level_button.collidepoint(mouse):
                    print("Level Select") # add level select later

    def update(self):
        pass

    def render(self):
        self.screen.fill(WHITE)
        title_text = font.render("Grid Path Game", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        self.screen.blit(title_text, title_rect)

        pygame.draw.rect(self.screen, (220,120,255), self.start_button)
        start_text = font.render("Start", True, BLACK)
        start_rect = start_text.get_rect(center=self.start_button.center)
        self.screen.blit(start_text, start_rect)

        pygame.draw.rect(self.screen, (0,20,255), self.level_button)
        level_text = font.render("Level", True, BLACK)
        level_rect = level_text.get_rect(center=self.level_button.center)
        self.screen.blit(level_text, level_rect)