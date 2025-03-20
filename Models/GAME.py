# import random

# class Tile:
#     def __init__(self, is_wall):
#         self.is_wall = is_wall  # True for wall, False for path

# class Maze:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.grid = [[Tile(True) for _ in range(width)] for _ in range(height)]
#         self.start = (0, 0)
#         self.end = (height - 1, width - 1)
#         self.create_path()
    
#     def create_path(self):
#         # This method will create a random path from start to finish
#         start = (0, 0)
#         end = (self.height - 1, self.width - 1)
#         self.grid[start[0]][start[1]].is_wall = False
#         self.grid[end[0]][end[1]].is_wall = False
        
#         current_position = start
#         while current_position != end:
#             direction = random.choice(['right', 'down'])
#             if direction == 'right' and current_position[1] < self.width - 1:
#                 current_position = (current_position[0], current_position[1] + 1)
#             elif direction == 'down' and current_position[0] < self.height - 1:
#                 current_position = (current_position[0] + 1, current_position[1])
#             self.grid[current_position[0]][current_position[1]].is_wall = False
    
#     def is_valid_move(self, position):
#         if 0 <= position[0] < self.height and 0 <= position[1] < self.width:
#             return not self.grid[position[0]][position[1]].is_wall
#         return False

#     def display_maze(self, current_position):
#         for i, row in enumerate(self.grid):
#             row_display = ''
#             for j, tile in enumerate(row):
#                 if (i, j) == current_position:
#                     row_display += 'P '
#                 elif (i, j) == self.start:
#                     row_display += 'S '
#                 elif (i, j) == self.end:
#                     row_display += 'E '
#                 else:
#                     row_display += '. ' if not tile.is_wall else '# '
#             print(row_display)
#         print()

# def play_maze_game():
#     maze = Maze(5, 5)
#     current_position = maze.start
#     visited_tiles = {current_position}
    
#     while current_position != maze.end or len(visited_tiles) < maze.width * maze.height:
#         maze.display_maze(current_position)
#         move = input("Enter move (up, down, left, right): ").strip().lower()
#         if move == "up":
#             new_position = (current_position[0] - 1, current_position[1])
#         elif move == "down":
#             new_position = (current_position[0] + 1, current_position[1])
#         elif move == "left":
#             new_position = (current_position[0], current_position[1] - 1)
#         elif move == "right":
#             new_position = (current_position[0], current_position[1] + 1)
#         else:
#             print("Invalid move. Try again.")
#             continue
        
#         if maze.is_valid_move(new_position) and new_position not in visited_tiles:
#             current_position = new_position
#             visited_tiles.add(current_position)
#         else:
#             print("Move not allowed or tile already visited. Try again.")
    
#     print("Congratulations! You've reached the end and covered all tiles.")

# play_maze_game()


