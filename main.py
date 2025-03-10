import pygame

# variable definition
WIDTH, HEIGHT = 620, 480



# Main Pygame loop integrating the Game State Manager

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("ONE_LINE")
    clock = pygame.time.Clock()
    

    running = True
    while running:
        dt = clock.tick(60)/1000.0






    pygame.quit()


if __name__ == "__main__":
    main()