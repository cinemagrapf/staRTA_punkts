import pygame

class Credits:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 40)
        self.text_lines = [
            "Game by: Your Name",
            "Art by: Artist Name",
            "Music by: Composer Name",
            "Thanks for playing!",
            " ",
            "Press ESC to return"
        ]
        self.scroll_speed = 1.5  # Smooth scrolling
        self.scroll_y = self.screen.get_height()

        #Load background image or gif
        """" """

    #Load background music
        """" """

    def draw(self):
        self.screen.fill((0, 0, 30))  # Dark blue background
        for i, text in enumerate(self.text_lines):
            label = self.font.render(text, True, (255, 255, 255))
            x = self.screen.get_width() // 2 - label.get_width() // 2
            y = self.scroll_y + i * 50
            self.screen.blit(label, (x, y))

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.screen.fill((0, 0, 30))
            self.draw()
            pygame.display.flip()
            self.scroll_y -= self.scroll_speed  # Move text up

            if self.scroll_y + len(self.text_lines) * 50 < 0:
                return "menu"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "menu"  # Go back to menu

            clock.tick(60)  # Limit FPS
