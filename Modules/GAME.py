import pygame

class Game:
    """Represents the main game logic, handling rendering, player movement, and event processing."""
    
    def __init__(self):
        """Initializes the game, setting up the maze, player position, and game state."""
        pygame.init()
        self.window = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("ONE_LINE")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Maze definition moved inside the class to encapsulate data
        self.ROW, self.COL = 6, 4
        self.maze = [
            [0,  0,  0,  2],
            [0, 1, 0,  0],
            [0, 0, 0,  0],
            [0,  0,  1,  0],
            [0,  0, 1, 0],
            [3,  0,  0,  0]
        ]
        
        # Player start and end positions
        self.START = (0, 3)
        self.END = (5, 0)
        
        self.player_pos = self.START
        self.visited = {self.START}

        # Calculate walkable tiles (Encapsulation: moved inside the class)
        self.walkable_tiles = sum(1 for row in self.maze for cell in row if cell != 1)

    def move_player(self, dx, dy):
        """Handles player movement while enforcing game rules (Encapsulation of movement logic)."""
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        # Ensure movement stays within bounds
        if 0 <= new_x < self.ROW and 0 <= new_y < self.COL:
            # Check if the new position is not a wall and hasn't been visited
            if self.maze[new_x][new_y] != 1 and (new_x, new_y) not in self.visited:
                self.player_pos = (new_x, new_y)
                self.visited.add(self.player_pos)
            else:
                print("Grid visited")

        # Check win condition
        if self.player_pos == self.END:
            if len(self.visited) == self.walkable_tiles:
                print("CONGRATS! You passed all tiles.")
            else:
                print("You missed some tiles.")

    def process_input(self):
        """Handles keyboard events to move the player."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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
        """Renders the game visuals, including the grid, player, and visited tiles."""
        self.window.fill((231, 245, 255))  # Background color
        font = pygame.font.SysFont("arial", 50)

        # Draw grid
        for i in range(self.ROW + 1):
            pygame.draw.line(self.window, (91, 135, 227), (0, i * (600/self.ROW)), (self.COL * (600/self.ROW), i * (600/self.ROW)), 3)
        for j in range(self.COL + 1):
            pygame.draw.line(self.window, (91, 135, 227), (j * (600/self.ROW), 0), (j * (600/self.ROW), self.ROW * (600/self.ROW)), 3)

        # Draw walls, start, and end positions
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.maze[i][j] == 1:
                    pygame.draw.rect(self.window, (0, 0, 57), (j * (600/self.ROW), i * (600/self.ROW), (600/self.ROW), (600/self.ROW)))
                elif (i, j) == self.END:
                    end_text = font.render("E", True, (175, 176, 255))
                    self.window.blit(end_text, ((j + 0.3) * (600/self.ROW), (i + 0.2) * (600/self.ROW)))

        # Draw visited path
        for x, y in self.visited:
            pygame.draw.circle(self.window, (200, 195, 230), ((y + 0.5) * (600/self.ROW), (x + 0.5) * (600/self.ROW)), 10)

        # Draw player
        x, y = self.player_pos
        pygame.draw.circle(self.window, (255, 206, 227), ((y + 0.5) * (600/self.ROW), (x + 0.5) * (600/self.ROW)), 32)

        pygame.display.update()

    def run(self):
        """Runs the main game loop until the player quits."""
        while self.running:
            self.process_input()
            self.render()
            self.clock.tick(30)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
