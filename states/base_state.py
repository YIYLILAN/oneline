# adopt from Mr Sullivan's Battleship, write a abstract class for all states and modify according to functionality

from abc import ABC, abstractmethod

class BaseState(ABC):
    def __init__(self, screen):
        self.screen = screen

    def enter(self):
        """Called when the state becomes active."""
        pass

    def exit(self):
        """Called when the state is exited."""
        pass

    @abstractmethod
    def handle_events(self, events):
        """
        Handle user input and events.

        Args:
            events (list): List of pygame events.
        """
        pass

    @abstractmethod
    def update(self):
        """Update the game logic for the state."""
        pass

    @abstractmethod
    def render(self):
        """Draw the state's elements on the screen."""
        pass

    

