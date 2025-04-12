import pygame, sys
from pygame.locals import *
import random

pygame.init()

# Constants
FPS = 60
FramePerSecond = pygame.time.Clock()
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Initialize the display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Need for Speed in Ohio")

# Load the street background image
background = pygame.image.load(r"C:\Users\Acer Nitro 5\Downloads\PygameTutorial_3_0\AnimatedStreet.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale the background to fit the screen

# Classes for Player, Enemy, and Coin
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Acer Nitro 5\Downloads\PygameTutorial_3_0\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = 10  # Starting speed of the enemy

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def increase_speed(self):
        self.speed += 0.02  # Increase speed when player collects enough coins

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Acer Nitro 5\Downloads\PygameTutorial_3_0\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self, weight=1):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Acer Nitro 5\Downloads\PygameTutorial_3_0\star.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize the coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(200, SCREEN_WIDTH - 40), 0)
        self.weight = weight  # Set coin's weight, randomize when created

    def move(self):
        self.rect.move_ip(0, 5)  # Move down 5 pixels per frame
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(200, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Initialize sprites
P1 = Player()
E1 = Enemy()

# Create a group of coins with random weights (1-3)
coins = [Coin(weight=random.randint(1, 3)) for _ in range(5)]

# Initialize score
coins_collected = 0
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()

    for coin in coins:
        coin.move()

    # Check for coin collection
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            coins_collected += coin.weight  # Add the weight of the collected coin to the score
            coin.rect.top = 0
            coin.rect.center = (random.randint(200, SCREEN_WIDTH - 40), 0)  # Reposition the coin
            coin.weight = random.randint(1, 3)  # Re-randomize the weight
    E1.move()
    

    # Check for game over
    if pygame.sprite.collide_rect(P1, E1):
        pygame.quit()
        sys.exit()

    # Increase enemy speed after collecting 10 weighted coins
    if coins_collected >= 10:
        E1.increase_speed()

    # Fill the screen with the background image
    DISPLAYSURF.blit(background, (0, 0))  # Draw the background

    # Draw all objects
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    for coin in coins:
        coin.draw(DISPLAYSURF)

    # Display the score
    score_text = font.render(f"Coins: {coins_collected}", True, BLACK)
    DISPLAYSURF.blit(score_text, (SCREEN_WIDTH - 150, 10))

    pygame.display.update()
    FramePerSecond.tick(FPS)
