import pygame
pygame.init()

from config.setting import WIDTH,HEIGHT

from Modules.GAME import Game




# Main Pygame loop integrating the Game State Manager

# def main():
    

    
    
    
#     running = True
#     while running:
#         clock.tick(60)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         pygame.display.flip()
#     pygame.quit()


if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ONE_LINE")
    game = Game(screen)
    game.run()
