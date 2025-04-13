import pygame
        
class Buttons:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))  # Define the rect using the image's size and position
        
    def press_key(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
