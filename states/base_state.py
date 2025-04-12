

from abc import ABC, abstractmethod

# --- BaseState Abstract Class ---
class BaseState(ABC):
    def __init__(self, screen):
        self.screen = screen

    def enter(self):
        pass

    def exit(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def render(self):
        pass
    

