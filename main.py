from states.GameManager import GameManager



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
    game_manager = GameManager()
    game_manager.run()
