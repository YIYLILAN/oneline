import pygame
from states.base_state import BaseState
from Modules.BUTTON import Buttons
from config.setting import level1, level2,level3,level4,level5

class LevelMenuState(BaseState):
    def __init__(self, screen, game):
        super().__init__(screen)
        self.game = game
        self.font = pygame.font.Font("assets/font/Pixeled.ttf", 28)
        self.level1_button = Buttons(100, 200, level1)
        self.level2_button = Buttons(100, 300, level2)
        self.level3_button = Buttons(100, 400, level3)
        self.level4_button = Buttons(100, 500, level4)
        self.level5_button = Buttons(100, 600, level5)

        # Create level buttons
        self.buttons = []
        for i in range(5):  # Levels 1 to 5
            x, y = 200, 150 + i * 80
            button_image = self.font.render(f" LEVEL {i+1} ", True, (255, 255, 255), (91, 135, 227))
            self.buttons.append(Buttons(x, y, button_image))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Iterate over all buttons to check for clicks
                for idx, button in enumerate(self.buttons):
                    if button.press_key():
                        self.game.load_level(idx + 1)  # Load the corresponding level
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.change_state(self.game.menu)

            

    def render(self):
        self.screen.fill((255, 255, 255))
        menu_title = self.font.render(" LEVELS ", True, (0, 0, 0))
        self.screen.blit(menu_title, (100, 40))

        for button in self.buttons:
            button.draw(self.screen)

        pygame.display.update()
