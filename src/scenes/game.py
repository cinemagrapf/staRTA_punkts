import pygame

# Game settings
GRAVITY = 0.5
JUMP_STRENGTH = -10
PLAYER_SPEED = 5

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((40, 60))
        self.image.fill((0, 255, 0))  # Green player
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = 0
        self.on_ground = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = JUMP_STRENGTH
            self.on_ground = False

    def apply_gravity(self, platforms):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y > 0:
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.on_ground = True
                break
        else:
            self.on_ground = False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Platform:
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill((150, 75, 0))  # Brown platform
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(100, 300)
        self.platforms = [Platform(50, 400, 700, 20)]  # One simple platform
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            self.screen.fill((135, 206, 250))  # Light blue background
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "menu"

            self.player.move(keys)
            self.player.apply_gravity(self.platforms)

            self.player.draw(self.screen)
            for platform in self.platforms:
                platform.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        return "menu"
