import pygame
import sys
import time
from config.setting import WIDTH,HEIGHT




# Main Pygame loop integrating the Game State Manager

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ONE_LINE")
    clock = pygame.time.Clock()
    
    
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()