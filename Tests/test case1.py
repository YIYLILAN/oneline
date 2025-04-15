import pygame
from unittest import mock
from GameManager import GameManager
from states.game_state import MazeGameState
from states.level_menu import LevelMenuState

def test_menu_buttons():
    game_manager = GameManager()
    menu_state = game_manager.get_menu_state()
    
    # Mock the screen and events
    mock_screen = mock.MagicMock()
    mock_event = mock.MagicMock()
    
    # Simulate pressing the Start button
    mock_event.type = pygame.MOUSEBUTTONDOWN
    mock_event.pos = (200, 260)  # Simulating click on the Start button
    menu_state.handle_events([mock_event])
    
    # Assert that the game state has changed to MazeGameState after clicking Start
    assert isinstance(game_manager.state, MazeGameState)
    
    # Simulate pressing the Level button
    mock_event.pos = (200, 360)  # Simulating click on the Level button
    menu_state.handle_events([mock_event])
    
    # Assert that the game state has changed to LevelMenuState
    assert isinstance(game_manager.state, LevelMenuState)

    # Simulate pressing the Quit button
    mock_event.pos = (200, 460)  # Simulating click on the Quit button
    menu_state.handle_events([mock_event])
    
    # Assert that the game has quit (should close the pygame window)
    mock_screen.quit.assert_called_once()
