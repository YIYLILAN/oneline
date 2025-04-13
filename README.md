# ONE_LINE
ONE_LINE is an interactive puzzle game that tests the player's problem-solving skills by navigating through a grid and occupying all the available cells. The objective is to complete each level by filling the grid in a continuous path, with no overlapping moves. Players must plan their moves strategically and use the available tools, such as the "reverse" and "reset" buttons, to achieve victory. The game features increasing levels of difficulty to provide a challenging and rewarding experience. The purpose of the game is to engage players with challenging puzzles that encourage logical thinking, while providing a simple and fun experience.

---Key Features---
Start/Level Buttons: The main screen displays the game's name and provides buttons to start the game or select levels.
Keyboard Navigation: Players use arrow keys to move around the grid.
Grid Occupation Mechanics: Players must occupy all tiles to complete a level, and the path they take must be continuous without overlaps.
Reverse Function: Players can backtrack to the last grid they occupied.
Reset Button: Players can reset the game state to its initial setup at any time.
Level Completion: Once all grids are filled, players are shown a "Level Complete" page with options to continue to the next level or return to the main menu.

---Prerequisites---
To run this project, player must have:
- Python 3.7 or higher
- Pygame library installed


Arrow keys: Use the arrow keys to navigate around the grid.
Left arrow: Move left
Right arrow: Move right
Up arrow: Move up
Down arrow: Move down

Reverse button: Press to backtrack to the last occupied grid.
Reset button: Press to reset the game and clear all moves.
Start button: Press to start the game or continue from where you left off.
Level button: Press to select the level to play.

---Functional Requirements and Implementation---

The main screen displays the game’s title and provides buttons for starting the game and selecting levels. These buttons are implemented using Pygame's event handling system.

Game Mechanics:
Players navigate the grid using the arrow keys. Each movement is recorded, and a continuous line is drawn to indicate the occupied grids. Overlapping grids trigger a notification, and unfilled grids at the end of the level trigger a "Still grids unoccupied" message.

Completion Criteria:
The game checks if all grids have been occupied. If any remain unoccupied, the game notifies the player.
Once all grids are filled, a "Level Complete" page is displayed with options to continue to the next level or return to the menu. This is controlled by checking if the grid is fully occupied and displaying the appropriate screen.

Reverse Function:
The reverse button allows the player to backtrack to the previous grid, implemented by storing the player’s moves in a stack and popping the last move when the button is pressed.

Reset Button:
The reset button restores the game to its initial state by clearing all the player’s moves and resetting the board.

Dynamic Level Generation: (Removed)
The initial idea was to generate levels dynamically to provide new challenges. However, due to time constraints, this feature was removed after confirming with Mr. Sullivan.
