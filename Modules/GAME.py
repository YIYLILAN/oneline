import pygame
from config.setting import reset_button, reverse_button
from states.cover_menu import MenuState
from states.game_state import MazeGameState
from states.level_menu import LevelMenuState

#Constants
ROW, COL = 6, 4
START = (0, 3)
END = (5, 0)
BG_COLOUR = (231, 245, 255)
GRID_COLOUR = (91, 135, 227)
WALL_COLOUR = (0, 0, 57)
PLAYER_COLOUR = (255, 206, 227)
END_COLOUR = (175, 176, 255)
FPS = 30

# --- Maze Grid ---
maze = [
    [0, 0, 0, 2],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [3, 0, 0, 0]
]

# Count walkable tiles
walkable_tiles = sum(1 for row in maze for cell in row if cell != 1)


# Base Game Class
class Game:
    """
    - Encapsulation: Contains core game logic (init, loop, input handling, etc.).
    - Inheritance: Other classes (mazeGame) can extend this class.
    """

    def __init__(self, screen, game_manager): 
        self.screen = screen
        self.game_manager = game_manager 
        self.menu = MenuState(self.screen, self.game_manager)
        self.level_menu = LevelMenuState(self.screen, self.game_manager)
        self.maze_game = None
        self.state = self.menu


    # def change_state(self, new_state):
    #     self.state.exit()
    #     self.state = new_state
    #     self.state.enter()

    def change_state(self, new_state):
        self.game_manager.change_state(new_state) #use the game manager to change states.


    def load_level(self, level_num):
        self.maze_game = MazeGameState(self.screen, self.game_manager, level_num)
        self.game_manager.change_state(self.maze_game)

    def process_input(self):
        """
        Handles player input
        - Polymorphism: This method is overridden in MazeGame to handle movement
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Exit game loop


    def render(self):
        #Draws game elements, to be overridden in subclasses
        self.window.fill(BG_COLOUR)
        pygame.display.update()

    def run(self):
        """
        -Encapsulation: Ensures that the game runs in a structured manner
        """
        while self.running:
            self.clock.tick(FPS)
            #self.process_input()
            
            events = pygame.event.get()
            self.state.handle_events(events)
            self.state.render()
            
        pygame.quit()
        


# --- Maze Game Class (Inherits from Game) ---
class MazeGame(Game):
    """
    The main class demonstration the game mechanic.

    -Inheritance: Extends the Game class to implement specific game logic.
    -Encapsulation: Keeps player position and game state management within the class.
    """

    def __init__(self):
        
        super().__init__()  # Calls the parent class constructor
        self.player_pos = START  # Player's position in the maze
        self.visited = {START}  # Set to track visited tiles

        self.path_stack = [self.player_pos]
        self.button_height = 80  # areas in the bottom for buttons


 
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

        # Check win condition
        if self.player_pos == END:
            if len(self.visited) == walkable_tiles:
                print("CONGRATS! U passed all tiles.")
            else:
                print(" U reached the end but didnt pass all tiles.")

    def reverse_move(self):
        if len(self.path_stack) > 1:
            self.path_stack.pop()
            self.player_pos = self.path_stack[-1]
            self.visited = set(self.path_stack)

    def reset_game(self):
        self.player_pos = self.start
        self.visited = {self.player_pos}
        self.path_stack = [self.player_pos]


    def process_input(self):
        """
        Handles user input for player movement.

        -Polymorphism: Overrides Game's process_input to add movement logic.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Properly quit game loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move_player(-1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move_player(1, 0)
                elif event.key == pygame.K_LEFT:
                    self.move_player(0, -1)
                elif event.key == pygame.K_RIGHT:
                    self.move_player(0, 1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.reverse_button.collidepoint(event.pos):
                    self.reverse_move()
                elif self.reset_button.collidepoint(event.pos):
                    self.reset_game()


    def render(self):
        self.screen.fill((255, 255, 250))

        rows, cols = len(self.maze), len(self.maze[0])
        usable_height = self.screen.get_height() - self.button_height
        cell_size = min(self.screen.get_width() // cols, usable_height // rows)

        offset_y = (usable_height - rows * cell_size) // 2  

        # draw maze
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                x = j * cell_size
                y = offset_y + i * cell_size
                rect = pygame.Rect(x, y, cell_size, cell_size)

                if cell == 1:
                    pygame.draw.rect(self.screen, (0, 0, 57), rect)
                elif cell == 2:
                    pygame.draw.rect(self.screen, (175, 255, 175), rect)
                elif cell == 3:
                    pygame.draw.rect(self.screen, (175, 176, 255), rect)

        # draw visited tiles
        for x, y in self.visited:
            pygame.draw.circle(self.screen, (200, 195, 230),
                (y * cell_size + cell_size // 2, offset_y + x * cell_size + cell_size // 2), 6)

        # draw player
        px, py = self.player_pos
        pygame.draw.circle(self.screen, (255, 206, 227),
            (py * cell_size + cell_size // 2, offset_y + px * cell_size + cell_size // 2), cell_size // 3)

        # draw button
        # Draw reverse and reset buttons using images
        self.reverse_rect = self.screen.blit(reverse_button, (60, self.screen.get_height() - 70))
        self.reset_rect = self.screen.blit(reset_button, (260, self.screen.get_height() - 70))

        pygame.display.update()



