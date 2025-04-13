import pygame
from Modules.GAME import Game
from config.setting import WIDTH,HEIGHT

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ONE_LINE")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state_stack = []
        self.current_level = 1

        self.game = Game(self.screen, self)
        self.state = self.game.menu

    def run(self):
        while self.running:
            self.clock.tick(60)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.state.handle_events(events)
            self.state.render()

            pygame.display.flip()

        pygame.quit()

    def change_state(self, new_state):
        if self.state:
            self.state.exit()
            self.state_stack.append(self.state)
        self.state = new_state
        self.state.enter()

    def pop_state(self):
        if self.state:
            self.state.exit()
        if self.state_stack:
            self.state = self.state_stack.pop()
            self.state.enter()

    def load_level(self, level_num):
        print(f"Loading Level {level_num}")
        self.current_level = level_num
        self.game.load_level(level_num)

    def get_menu_state(self):
        return self.game.menu

    def get_level_menu(self):
        return self.game.level_menu

    def get_maze_game(self):
        return self.game.maze_game
