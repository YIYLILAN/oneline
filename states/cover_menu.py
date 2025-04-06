import pygame
from states.base_state import BaseState
from config.setting import title, start_button, level_button, quit_button
from Modules.BUTTON import Buttons

class MenuState(BaseState):
    def __init__(self, screen, game):
        super().__init__(screen)
        self.game = game
        # self.font = pygame.font.SysFont("arial", 50)
        self.START_button = Buttons(200,260,start_button)
        self.LEVEL_button = Buttons(200, 360 ,level_button)
        self.QUIT_button = Buttons(200, 460 ,quit_button)

 


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.LEVEL_button.press_key():
                    self.game.change_state(self.game.level_menu)
                    
                if self.START_button.press_key():
                    self.game.change_state(self.game.maze_game)

                elif self.QUIT_button.press_key():
                    pygame.quit()
                    exit()


    def render(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(title, title.get_rect(center=(200, 120)))

        self.screen.blit(self.START_button.image, self.START_button.rect)
        self.screen.blit(self.LEVEL_button.image, self.LEVEL_button.rect)
        self.screen.blit(self.QUIT_button.image, self.QUIT_button.rect)


        pygame.display.update()
