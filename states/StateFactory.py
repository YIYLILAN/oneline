from states.cover_menu import MenuState
from states.game_state import MazeGameState
from states.level_menu import LevelMenuState


# Base Game Class
class StateFactory:
    def __init__(self, screen, game_manager): 
        self.screen = screen
        self.game_manager = game_manager 
        self.menu = MenuState(self.screen, self.game_manager)
        self.level_menu = LevelMenuState(self.screen, self.game_manager)
        self.maze_game = None
        self.state = self.menu

    def change_state(self, new_state):
        self.game_manager.change_state(new_state) #use the game manager to change states.


    def load_level(self, level_num):
        self.maze_game = MazeGameState(self.screen, self.game_manager, level_num)
        self.game_manager.change_state(self.maze_game)
