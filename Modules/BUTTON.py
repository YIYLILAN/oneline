import pygame
from GAME import Game

class Buttons(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))


    def draw(self):
        Game.blit(self.image,(self.rect.x,self.rect.y))
        
    def press_key(self):
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check if mouse clicked
        if pygame.mouse.get_pressed()[0] and pos[0] in range(self.rect.x, self.rect.x + self.image.get_width()) and pos[1] in range(self.rect.y, self.rect.y + self.image.get_height()):
            return True
        else:
            return False