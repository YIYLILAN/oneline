import pygame
from states.base_state import BaseState
from Modules.BUTTON import Buttons

class LevelMenuState(BaseState):
    def __init__(self, screen, game):
        super().__init__(screen)
        self.game = game
        self.font = pygame.font.Font("assets/font/Pixeled.ttf", 28)

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
                for idx, button in enumerate(self.buttons):
                    if button.press_key():
                        print(f"Level {idx + 1} selected.")
                        self.game.load_level(idx+1) 
                        self.game.change_state(self.game.maze_game)
                        # TODO: Load level logic here

    def render(self):
        self.screen.fill((230, 240, 255))
        title = self.font.render(" LEVELS ", True, (0, 0, 0))
        self.screen.blit(title, (140, 40))

        for button in self.buttons:
            button.draw(self.screen)

        pygame.display.update()
