import pygame
from states.base_state import BaseState
from config.LEVELS import LEVELS, find_tile, count_walkable
from Modules.BUTTON import Buttons
from config.setting import reverse_button, reset_button

class MazeGameState(BaseState):
    def __init__(self, screen, game_manager, level):
        super().__init__(screen)
        self.game_manager = game_manager
        self.level = level
        self.maze = LEVELS[level]  # Load maze layout for the current level
        self.start = find_tile(self.maze, 2)  # Find start tile (marked with '2')
        self.end = find_tile(self.maze, 3)    # Find end tile (marked with '3')
        self.player_pos = self.start
        self.visited = {self.player_pos}      # Track visited tiles
        self.path_stack = [self.player_pos]   # Stack for reverse movement
        self.walkable_tiles = count_walkable(self.maze)  # Number of valid tiles to step on

        self.button_height = 80

        # UI buttons for reverse and reset functionality
        self.reverse_button = Buttons(100, self.screen.get_height() - 40, reverse_button)
        self.reset_button = Buttons(300, self.screen.get_height() - 40, reset_button)

        # Feedback system for temporary messages like "Invalid move"
        self.feedback_message = ""
        self.feedback_timer = 0

        self.level_complete = False
        self.continue_button = None
        self.menu_button = None

    def enter(self):
        print(f"Entered MazeGameState for Level {self.level}")

    def move_player(self, dx, dy):
        # Prevent movement if level is already complete
        if self.level_complete:
            return

        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        new_pos = (new_x, new_y)

        # Check boundaries and whether the tile is walkable and unvisited
        if 0 <= new_x < len(self.maze) and 0 <= new_y < len(self.maze[0]):
            if self.maze[new_x][new_y] != 1 and new_pos not in self.visited:
                self.player_pos = new_pos
                self.visited.add(new_pos)
                self.path_stack.append(new_pos)
                self.feedback_message = ""
            elif new_pos in self.visited:
                self.feedback_message = "Tile already visited"
                self.feedback_timer = pygame.time.get_ticks()
        else:
            self.feedback_message = "Invalid move"
            self.feedback_timer = pygame.time.get_ticks()

        # Check for win condition: reached end AND all walkable tiles visited
        if self.player_pos == self.end:
            if len(self.visited) == self.walkable_tiles:
                self.feedback_message = "Level Complete!"
                self.level_complete = True
            else:
                self.feedback_message = "You reached the end but didn't pass all tiles."
            self.feedback_timer = pygame.time.get_ticks()

    def reverse_move(self):
        # Undo last move if more than one tile has been visited
        if len(self.path_stack) > 1:
            self.path_stack.pop()
            self.player_pos = self.path_stack[-1]
            self.visited = set(self.path_stack)
            self.feedback_message = ""

    def reset_game(self):
        # Reset game to initial state
        self.player_pos = self.start
        self.visited = {self.player_pos}
        self.path_stack = [self.player_pos]
        self.feedback_message = ""
        self.level_complete = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_manager.pop_state()  # Return to previous state
                elif event.key == pygame.K_UP:
                    self.move_player(-1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move_player(1, 0)
                elif event.key == pygame.K_LEFT:
                    self.move_player(0, -1)
                elif event.key == pygame.K_RIGHT:
                    self.move_player(0, 1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.level_complete:
                    # After win, either continue to next level or return to menu
                    if self.continue_button and self.continue_button.press_key():
                        next_level = self.level + 1
                        if next_level in LEVELS:
                            self.game_manager.load_level(next_level)
                    elif self.menu_button and self.menu_button.press_key():
                        self.game_manager.change_state(self.game_manager.get_menu_state())
                else:
                    # During play: reverse or reset buttons
                    if self.reverse_button.press_key():
                        self.reverse_move()
                    elif self.reset_button.press_key():
                        self.reset_game()

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear screen

        # Calculate grid cell size and centering
        rows, cols = len(self.maze), len(self.maze[0])
        usable_height = self.screen.get_height() - self.button_height - 60
        usable_width = self.screen.get_width() - 40
        cell_size = min(usable_width // cols, usable_height // rows)
        total_grid_height = rows * cell_size
        total_grid_width = cols * cell_size
        offset_x = (self.screen.get_width() - total_grid_width) // 2
        offset_y = 40 + (usable_height - total_grid_height) // 2

        # Draw the maze grid
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                x = offset_x + j * cell_size
                y = offset_y + i * cell_size
                rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)

                # Draw wall, start, or end tile
                if cell == 1:
                    pygame.draw.rect(self.screen, (255, 255, 255), rect)  # Wall
                elif cell == 2:
                    pygame.draw.rect(self.screen, (175, 255, 175), rect)  # Start
                elif cell == 3:
                    pygame.draw.rect(self.screen, (175, 176, 255), rect)  # End

        # Draw all visited tiles as small dots
        for x, y in self.visited:
            draw_x = offset_x + y * cell_size + cell_size // 2
            draw_y = offset_y + x * cell_size + cell_size // 2
            pygame.draw.circle(self.screen, (200, 195, 230), (draw_x, draw_y), 6)

        # Draw player as a large colored circle
        px, py = self.player_pos
        pygame.draw.circle(self.screen, (255, 206, 227),
            (offset_x + py * cell_size + cell_size // 2, offset_y + px * cell_size + cell_size // 2), cell_size // 3)

        # ESC tip in top-left
        font = pygame.font.SysFont("arial", 12)
        esc_msg = font.render("ESC to Return", True, (255, 255, 255))
        self.screen.blit(esc_msg, (10, 10))

        # Feedback message (e.g., "Invalid move", "Level Complete!")
        if self.feedback_message and pygame.time.get_ticks() - self.feedback_timer < 2000:
            feedback_font = pygame.font.SysFont("arial", 18)
            text = feedback_font.render(self.feedback_message, True, (255, 255, 255))
            self.screen.blit(text, ((self.screen.get_width() - text.get_width()) // 2, 20))

        if self.level_complete:
            # Level complete UI with Continue and Menu options
            big_font = pygame.font.Font("assets/font/Pixeled.ttf", 25)
            win_text = big_font.render("LEVEL COMPLETE!", True, (0, 0, 200))
            self.screen.blit(win_text, ((self.screen.get_width() - win_text.get_width()) // 2, 190))

            # Continue button setup
            cont_img = pygame.Surface((200,40))
            cont_img.fill((91, 135, 227))
            cont_font = pygame.font.SysFont("chicago", 30)
            cont_text = cont_font.render("Continue", True, (255, 255, 255))
            cont_img.blit(cont_text, ((cont_text.get_width()) / 2, 8))

            # Menu button setup
            menu_img = pygame.Surface((200, 40))
            menu_img.fill((91, 135, 227))
            menu_font = pygame.font.SysFont("chicago", 30)
            menu_text = menu_font.render("Menu", True, (255, 255, 255))
            menu_img.blit(menu_text, ((menu_text.get_width()) / 2, 8))

            self.continue_button = Buttons(240, 320, cont_img)
            self.menu_button = Buttons(240, 380, menu_img)

            self.continue_button.draw(self.screen)
            self.menu_button.draw(self.screen)
        else:
            # In-game utility buttons
            self.reverse_button.draw(self.screen)
            self.reset_button.draw(self.screen)

        pygame.display.update()  # Refresh display with all new drawings
