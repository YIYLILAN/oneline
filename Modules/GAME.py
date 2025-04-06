import pygame
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
WIDTH, HEIGHT = 400, 600
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

    def __init__(self, screen):
        """Initialiases the game window and clock"""
        self.screen = screen
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ONE_LINE")
        self.clock = pygame.time.Clock()
        self.running = True  # make sure the game loop running
        

        self.menu = MenuState(self.screen, self)
        self.level_menu = LevelMenuState(self.screen, self)
        self.maze_game = None
        self.state = self.menu

    def change_state(self, new_state):
        self.state.exit()
        self.state = new_state
        self.state.enter()

    def load_level(self, level_num):
        self.maze_game = MazeGameState(self.screen, self, level_num)
        self.change_state(self.maze_game)


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
        """
        Initialises the maze game by calling the Game constructor and setting player variables.
        """
        super().__init__()  # Calls the parent class constructor
        self.player_pos = START  # Player's position in the maze
        self.visited = {START}  # Set to track visited tiles

    def move_player(self, dx, dy):
        """
        Moves the player while checking walls and visited cells.

        -Encapsulation: Player movement logic is inside the MazeGame class.
        """
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        # Check if within bounds and not a wall
        if 0 <= new_x < ROW and 0 <= new_y < COL and maze[new_x][new_y] != 1:
            if (new_x, new_y) not in self.visited:
                self.player_pos = (new_x, new_y)
                self.visited.add(self.player_pos)
            else:
                print("Grid already visited")

        # Check win condition
        if self.player_pos == END:
            if len(self.visited) == walkable_tiles:
                print("CONGRATS! U passed all tiles.")
            else:
                print(" U reached the end but didnt pass all tiles.")

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

    def render(self):
        """
        Draws the game grid, walls, player, and visited tiles.

        -Polymorphism: Overrides Game's render method to display specific visuals.
        """
        self.window.fill(BG_COLOUR)
        font = pygame.font.SysFont("arial", 50)

        # Draw grid
        for i in range(ROW + 1):
            pygame.draw.line(self.window, GRID_COLOUR, (0, i * (HEIGHT/ROW)), (COL * (HEIGHT/ROW), i * (HEIGHT/ROW)), 3)
        for j in range(COL + 1):
            pygame.draw.line(self.window, GRID_COLOUR, (j * (HEIGHT/ROW), 0), (j * (HEIGHT/ROW), ROW * (HEIGHT/ROW)), 3)

        # Draw walls, start, and end
        for i in range(ROW):
            for j in range(COL):
                if maze[i][j] == 1:  # Wall
                    pygame.draw.rect(self.window, WALL_COLOUR, (j * (HEIGHT/ROW), i * (HEIGHT/ROW), (HEIGHT/ROW), (HEIGHT/ROW)))
                elif (i, j) == END:  # End point
                    end_text = font.render("E", True, END_COLOUR)
                    self.window.blit(end_text, ((j + 0.3) * (HEIGHT/ROW), (i + 0.2) * (HEIGHT/ROW)))

        # Draw visited path
        for x, y in self.visited:
            pygame.draw.circle(self.window, (200, 195, 230), ((y + 0.5) * (HEIGHT/ROW), (x + 0.5) * (HEIGHT/ROW)), 10)

        # Draw player
        x, y = self.player_pos
        pygame.draw.circle(self.window, PLAYER_COLOUR, ((y + 0.5) * (HEIGHT/ROW), (x + 0.5) * (HEIGHT/ROW)), 32)

        pygame.display.update()


