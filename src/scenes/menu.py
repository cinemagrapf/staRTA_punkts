import pygame
#import os

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.options = ["Start Game", "Credits", "Quit"]
        self.selected_index = 0



        # Load and  resize GIF frames
        self.bg_frames = self.load_gif("../assets/images/menu_background/background.gif")
        self.bg_index = 0
        self.bg_timer = pygame.time.get_ticks()  # Track time for smooth animation

        # Set borderless fullscreen
        self.set_fullscreen()

        # Load sounds
        self.select_sound = pygame.mixer.Sound("../assets/sounds/select.wav")
        self.confirm_sound = pygame.mixer.Sound("../assets/sounds/confirm.wav")

        # Load background music
        pygame.mixer.music.load("../assets/sounds/menu_music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def set_fullscreen(self):
        display_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.NOFRAME)
        self.resize_frames((display_info.current_w, display_info.current_h))

    def load_gif(self, gif_path):
        """Extract frames from a GIF and return as a list of Pygame images."""
        frames = []
        try:
            from PIL import Image
            gif = Image.open(gif_path)

            while True:
                frame = gif.convert("RGB")
                frame = pygame.image.fromstring(frame.tobytes(), frame.size, "RGB")
                frame = pygame.transform.scale(frame, self.screen.get_size())  # Scale to screen size
                frames.append(frame)
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass  # End of GIF frames
        return frames

    def resize_frames(self, new_size):
        """Resize all frames to match the new window size."""
        self.bg_frames = [pygame.transform.scale(frame, new_size) for frame in self.bg_frames]

    def draw(self):
        # Smooth GIF animation (change frame every 100ms)
        if self.bg_frames and pygame.time.get_ticks() - self.bg_timer > 100:
            self.bg_index = (self.bg_index + 1) % len(self.bg_frames)
            self.bg_timer = pygame.time.get_ticks()

        # Draw resized background
        if self.bg_frames:
            self.screen.blit(self.bg_frames[self.bg_index], (0, 0))

        # Draw menu text
        for i, text in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_index else (200, 200, 200)
            label = self.font.render(text, True, color)
            x = self.screen.get_width() // 2 - label.get_width() // 2
            y = (self.screen.get_height() // 2 - label.get_height() // 2)+i*60#200 + i * 60
            self.screen.blit(label, (x, y))

    def run(self):
        running = True
        while running:
            self.draw()
            pygame.display.flip()

            mouse_x, mouse_y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    self.set_fullscreen()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                        self.select_sound.play()
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                        self.select_sound.play()
                    if event.key == pygame.K_RETURN:
                        self.confirm_sound.play()
                        pygame.time.delay(200)
                        if self.selected_index == 0:
                            return "playing"
                        elif self.selected_index == 1:
                            return "credits"
                        elif self.selected_index == 2:
                            return "quit"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, text in enumerate(self.options):
                        label = self.font.render(text, True, (255, 255, 255))
                        x = self.screen.get_width() // 2 - label.get_width() // 2
                        y = 200 + i * 60
                        if x <= mouse_x <= x + label.get_width() and y <= mouse_y <= y + 50:
                            self.selected_index = i
                            self.confirm_sound.play()
                            pygame.time.delay(200)
                            if i == 0:
                                return "playing"
                            elif i == 1:
                                return "credits"
                            elif i == 2:
                                return "quit"

        return "menu"
