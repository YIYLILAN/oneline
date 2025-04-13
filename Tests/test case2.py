import pygame
from unittest import mock
from states.GameManager import GameManager
from states.game_state import MazeGameState


def test_level_buttons():
    game_manager = GameManager()
    level_menu_state = game_manager.get_level_menu()
    
    # Mock the screen and events
    mock_screen = mock.MagicMock()
    mock_event = mock.MagicMock()
    
    # Simulate pressing the Level 1 button
    mock_event.type = pygame.MOUSEBUTTONDOWN
    mock_event.pos = (200, 200)  # Simulating click on Level 1 button
    level_menu_state.handle_events([mock_event])
    
    # Assert that the game has loaded level 1 and the state is MazeGameState
    assert game_manager.current_level == 1
    assert isinstance(game_manager.state, MazeGameState)
    
    # Simulate pressing the Level 2 button
    mock_event.pos = (200, 280)  # Simulating click on Level 2 button
    level_menu_state.handle_events([mock_event])
    
    # Assert that the game has loaded level 2 and the state is MazeGameState
    assert game_manager.current_level == 2
    assert isinstance(game_manager.state, MazeGameState)
