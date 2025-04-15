from abc import ABC, abstractmethod

# --- BaseState Abstract Class ---
# This is the foundation for all game states (menus, gameplay, etc.).
# It enforces a consistent interface (enter, exit, handle_events, render).
class BaseState(ABC):
    def __init__(self, screen):
        self.screen = screen

    # Called when entering this state
    def enter(self):
        pass

    # Called when exiting this state
    def exit(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def render(self):
        pass
