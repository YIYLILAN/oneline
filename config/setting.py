import pygame

# variable definition

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH,HEIGHT = 480,600

font = font = pygame.font.Font(None, 36)

title = pygame.image.load("/Users/Admin/Documents/Y12 ATAR/CS/dev/oneline/assets/image/title.png")
title = pygame.transform.scale_by(title, 0.16)

start_button = pygame.image.load("/Users/Admin/Documents/Y12 ATAR/CS/dev/oneline/assets/image/start.png")
start_button = pygame.transform.scale_by(start_button, 0.15)

level_button = pygame.image.load("/Users/Admin/Documents/Y12 ATAR/CS/dev/oneline/assets/image/level.png")
level_button = pygame.transform.scale_by(level_button, 0.15)

quit_button = pygame.image.load("/Users/Admin/Documents/Y12 ATAR/CS/dev/oneline/assets/image/exit.png")
quit_button = pygame.transform.scale_by(quit_button, 0.10
)