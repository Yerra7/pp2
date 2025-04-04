import pygame, sys
from pygame.locals import *
import random

pygame.init()
FPS = 60
FramePerSecond = pygame.time.Clock()
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Need for speed in Ohio")



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Acer Nitro 5\Downloads\PygameTutorial_3_0\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
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
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Acer Nitro 5\Downloads\PygameTutorial_3_0\star.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize the coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 5)  # Move down 5 pixels per frame
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

C1 = Coin()
P1 = Player()
E1 = Enemy()

score = 0
font = pygame.font.Font(None, 36)
score_text = font.render(f"Score: {score}", True, BLACK)
DISPLAYSURF.blit(score_text, (10, 10))
if pygame.sprite.collide_rect(P1, C1):
    score += 1  # Increase the score
    C1.rect.top = 0  # Reset the coin to the top
    C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # New position

if pygame.sprite.collide_rect(P1, E1):
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()
    C1.move()

    # Check for coin collection
    if pygame.sprite.collide_rect(P1, C1):
        score += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Check for game over
    if pygame.sprite.collide_rect(P1, E1):
        pygame.quit()
        sys.exit()

    DISPLAYSURF.fill(WHITE)
    
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    C1.draw(DISPLAYSURF)

    # Display the score
    score_text = font.render(f"Score: {score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    pygame.display.update()
    FramePerSecond.tick(FPS)
