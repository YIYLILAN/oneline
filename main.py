import pygame

# Main Pygame loop integrating the Game State Manager

def main():
    pygame.init()

    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("ONE_LINE")
    clock = pygame.time.Clock()
    

    running = True
    while running:
        dt = clock.tick(60)/1000.0






    pygame.quit()


if __name__ == "__main__":
    main()