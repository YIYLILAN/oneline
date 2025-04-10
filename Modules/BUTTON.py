import pygame

# class Buttons(pygame.sprite.Sprite):
#     def __init__(self, x, y, image):
#         super().__init__()
#         self.image = image
#         self.rect = self.image.get_rect(center=(x, y))


#     def draw(self, screen):
#         screen.blit(self.image,(self.rect.x,self.rect.y))
        
#     def press_key(self):
#         #get mouse position
#         pos = pygame.mouse.get_pos()

#         #check if mouse clicked
#         if pygame.mouse.get_pressed()[0] and pos[0] in range(self.rect.x, self.rect.x + self.image.get_width()) and pos[1] in range(self.rect.y, self.rect.y + self.image.get_height()):
#             return True
#         else:
#             return False
        
class Buttons:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))  # Define the rect using the image's size and position

    def press_key(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)  # Check if the mouse position is within the button's rect

    def draw(self, screen):
        screen.blit(self.image, self.rect)
