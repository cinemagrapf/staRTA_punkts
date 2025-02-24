import pygame
from src.scenes.menu import Menu
from src.scenes.game import Game
from src.scenes.credits import Credits

# Initialize Pygame
pygame.init()

# Game Constants
FPS = 30

# Create Game Window
screen = pygame.display.set_mode()
pygame.display.set_caption("staRTA punkts")

# Define Game States
MENU, PLAYING, CREDITS, QUIT = "menu", "playing", "credits", "quit"

def main():
    clock = pygame.time.Clock()
    running = True
    game_state = MENU  # Start in the menu

    # Create Scene Objects
    menu = Menu(screen)
    game = Game(screen)
    credits = Credits(screen)

    while running:
        screen.fill((0, 0, 0))  # Clear screen each frame

        # Game State Management
        if game_state == MENU:
            game_state = menu.run()
        elif game_state == PLAYING:
            game_state = game.run()
        elif game_state == CREDITS:
            game_state = credits.run()
        elif game_state == QUIT:
            running = False

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
