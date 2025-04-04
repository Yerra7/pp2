import pygame  
import sys  # Importing the sys module to interact with the system
import copy  # Importing the copy module to create copies of objects
import random  # Importing the random module to work with random numbers
import time  # Importing the time module to work with time

pygame.init()  # Initializing Pygame

# Setting game parameters
scale = 15  # Scale of the objects
score = 0  # Player's score
level = 0  # Game level
SPEED = 10  # Snake speed

food_x = 10  # x-coordinate of food
food_y = 10  # y-coordinate of food

# Creating a window to display the game
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")  # Setting window title
clock = pygame.time.Clock()  # Creating Clock object to manage time in the game

# Defining colors in RGB format
background_top = (0, 50, 100)  # Top background color
background_bottom = (50, 0, 0)  # Bottom background color
snake_colour = (255, 137, 0)  # Snake color
food_colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # Food color (random)
snake_head = (255, 247, 0)  # Snake head color
font_colour = (255, 255, 255)  # Font color
defeat_colour = (255, 0, 0)  # Game over text color

# Defining Snake class to create snake object
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start  # Initial x-coordinate of snake
        self.y = y_start  # Initial y-coordinate of snake
        self.w = 15  # Width of snake
        self.h = 15  # Height of snake
        self.x_dir = 1  # Direction of movement along x-axis (1 - right, -1 - left)
        self.y_dir = 0  # Direction of movement along y-axis (1 - down, -1 - up)
        self.history = [[self.x, self.y]]  # Snake's movement history
        self.length = 1  # Snake's length

    # Method to reset the snake's state
    def reset(self):
        self.x = 500 / 2 - scale  # Reset x to center
        self.y = 500 / 2 - scale  # Reset y to center
        self.w = 15  # Reset width
        self.h = 15  # Reset height
        self.x_dir = 1  # Reset x-direction
        self.y_dir = 0  # Reset y-direction
        self.history = [[self.x, self.y]]  # Reset movement history
        self.length = 1  # Reset snake length

    # Method to display snake on screen
    def show(self):
        for i in range(self.length):
            if not i == 0:
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))

    # Method to check if the snake has eaten the food
    def check_eaten(self):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True

    # Method to check if the snake has reached a new level
    def check_level(self):
        global level
        if self.length % 5 == 0:
            return True

    # Method to grow the snake
    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    # Method to check if the snake collides with its own tail
    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    # Method to update snake's coordinates
    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

# Defining Food class to create food object
class Food:
    # Method to set a new food position on the screen
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, int(500 / scale) - 1) * scale
        food_y = random.randrange(1, int(500 / scale) - 1) * scale

    # Method to display food on the screen
    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))

# Function to display player's score
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))

# Function to display game level
def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))

# Main game loop
def gameLoop():
    global score
    global level
    global SPEED

    snake = Snake(500 / 2, 500 / 2)  # Creating snake object
    food = Food()  # Creating food object
    food.new_location()  # Setting the initial position of food

    while True:  # Infinite game loop
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:  # If user closes the window
                pygame.quit()  # Exit Pygame
                sys.exit()  # Exit the program
            if event.type == pygame.KEYDOWN:  # If user presses a key
                if event.key == pygame.K_q:  # If 'Q' is pressed
                    pygame.quit()  # Exit Pygame
                    sys.exit()  # Exit the program
                if snake.y_dir == 0:  # If snake moves horizontally
                    if event.key == pygame.K_UP:  # If UP arrow key is pressed
                        snake.x_dir = 0  # Set horizontal movement to 0
                        snake.y_dir = -1  # Set vertical movement upwards
                    if event.key == pygame.K_DOWN:  # If DOWN arrow key is pressed
                        snake.x_dir = 0  # Set horizontal movement to 0
                        snake.y_dir = 1  # Set vertical movement downwards

                if snake.x_dir == 0:  # If snake moves vertically
                    if event.key == pygame.K_LEFT:  # If LEFT arrow key is pressed
                        snake.x_dir = -1  # Set horizontal movement to left
                        snake.y_dir = 0  # Set vertical movement to 0
                    if event.key == pygame.K_RIGHT:  # If RIGHT arrow key is pressed
                        snake.x_dir = 1  # Set horizontal movement to right
                        snake.y_dir = 0  # Set vertical movement to 0

        # Filling background with gradient (modified for a smoother color transition)
        for y in range(500):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / 500,
                background_top[1] + (background_bottom[1] - background_top[1]) * (500 - y) / 500,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))

        snake.show()  # Display snake on screen
        snake.update()  # Update snake's position
        food.show()  # Display food on screen
        show_score()  # Display player score
        show_level()  # Display game level

        if snake.check_eaten():  # If snake eats food
            food.new_location()  # Set new food position
            score += random.randint(1, 5)  # Increase score by a random amount
            snake.grow()  # Grow snake

        if snake.check_level():  # If snake reaches a new level
            food.new_location()  # Set new food position
            level += 1  # Increase level
            SPEED += 1  # Increase speed
            snake.grow()  # Grow snake

        if snake.death():  # If snake collides with its own tail
            score = 0  # Reset score
            level = 0  # Reset level
            font = pygame.font.SysFont(None, 100)  # Font for displaying text
            text = font.render("Game Over!", True, defeat_colour)  # Create "Game Over!" text
            display.blit(text, (50, 200))  # Display text on screen
            pygame.display.update()  # Update screen
            time.sleep(3)  # Pause before resetting the game
            snake.reset()  # Reset snake's state

        if snake.history[0][0] > 500:  # If snake goes off the right side
            snake.history[0][0] = 0  # Move snake to left side

        if snake.history[0][0] < 0:  # If snake goes off the left side
            snake.history[0][0] = 500  # Move snake to right side

        if snake.history[0][1] > 500:  # If snake goes off the bottom
            snake.history[0][1] = 0  # Move snake to top

        if snake.history[0][1] < 0:  # If snake goes off the top
            snake.history[0][1] = 500  # Move snake to bottom

        pygame.display.update()  # Update display
        clock.tick(SPEED)  # Control game speed

gameLoop()  # Start the game loop
