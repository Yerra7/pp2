import pygame   
import sys  # Importing the sys module for system interactions
import copy  # Importing the copy module for creating object copies
import random  # Importing the random module for working with random numbers
import time  # Importing the time module for time-related functions
import sqlite3

def get_or_create_user():
    conn = sqlite3.connect("snake_game.db")
    cursor = conn.cursor()

    username = input("Enter your username: ").strip()

    # Check if user exists
    cursor.execute("SELECT id, level FROM user WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        user_id, level = result
        print(f"Welcome back, {username}! You're currently on level {level}.")
    else:
        # Create new user
        cursor.execute("INSERT INTO user (username) VALUES (?)", (username,))
        conn.commit()
        user_id = cursor.lastrowid
        level = 0
        print(f"New user created: {username}. Starting at level {level}.")

    conn.close()
    return user_id, username, level
def save_user_progress(user_id, level, score):
    conn = sqlite3.connect("snake_game.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET level = ?, score = ? WHERE id = ?", (level, score, user_id))
    conn.commit()
    conn.close()

def update_user_level(user_id, new_level):
    conn = sqlite3.connect("snake_game.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET level = ? WHERE id = ?", (new_level, user_id))
    conn.commit()
    conn.close()

# Example use
if __name__ == "__main__":
    user_id, username, level = get_or_create_user()

pygame.init()  # Initializing Pygame

# Setting up game parameters
scale = 15  # Object scale
score = 0  # Player's score
level = 0  # Game level
SPEED = 10  # Snake's speed

food_x = 10  # x-coordinate for the food
food_y = 10  # y-coordinate for the food

# Creating a game window
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")  # Setting the window title
clock = pygame.time.Clock()  # Creating a Clock object to manage game time

# Defining colors in RGB format
background_top = (0, 0, 50)  # Top part of the background gradient color
background_bottom = (50, 50, 50)  # Bottom part of the background gradient color (changed)
snake_colour = (255, 137, 0)  # Snake color
food_colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # Random food color
snake_head = (255, 247, 0)  # Snake head color
font_colour = (255, 255, 255)  # Font color
defeat_colour = (255, 0, 0)  # Color for "Game Over" message

# Defining the Snake class to create the snake object
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start  # Snake's initial x-coordinate
        self.y = y_start  # Snake's initial y-coordinate
        self.w = 15  # Snake's width
        self.h = 15  # Snake's height
        self.x_dir = 1  # Direction of movement on the x-axis (1 - right, -1 - left)
        self.y_dir = 0  # Direction of movement on the y-axis (1 - down, -1 - up)
        self.history = [[self.x, self.y]]  # Snake's movement history
        self.length = 1  # Snake's length

    # Method to reset the snake's state
    def reset(self):
        self.x = 500 / 2 - scale  # Resetting snake's position to the center on the x-axis
        self.y = 500 / 2 - scale  # Resetting snake's position to the center on the y-axis
        self.w = 15  # Resetting snake's width
        self.h = 15  # Resetting snake's height
        self.x_dir = 1  # Resetting direction on the x-axis
        self.y_dir = 0  # Resetting direction on the y-axis
        self.history = [[self.x, self.y]]  # Resetting movement history
        self.length = 1  # Resetting snake's length

    # Method to show the snake on the screen
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

    # Method to check if a new level has been reached
    def check_level(self):
        global level
        if self.length % 5 == 0:
            return True

    # Method to increase the snake's length
    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    # Method to check for collision with its own tail
    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    # Method to update the snake's coordinates
    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

# Defining the Food class to create the food object
class Food:
    # Method to set a new position for the food on the screen
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, int(500 / scale) - 1) * scale
        food_y = random.randrange(1, int(500 / scale) - 1) * scale

    # Method to show the food on the screen
    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))

# Function to display the player's score
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))

# Function to display the game level
def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))

# Main game loop
def gameLoop():
    global score
    global level
    global SPEED

    snake = Snake(500 / 2, 500 / 2)  # Creating a snake object
    food = Food()  # Creating a food object
    food.new_location()  # Setting the initial food position

    while True:  # Infinite game loop
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:  # If the user closes the window
                pygame.quit()  # Quit Pygame
                sys.exit()  # Exit the program
            if event.type == pygame.KEYDOWN:  # If the user presses a key
                if event.key == pygame.K_q:  # If Q is pressed
                    pygame.quit()  # Quit Pygame
                    sys.exit()  # Exit the program
                if snake.y_dir == 0:  # If the snake is moving horizontally
                    if event.key == pygame.K_UP:  # If UP is pressed
                        snake.x_dir = 0  # Set horizontal direction to 0
                        snake.y_dir = -1  # Set vertical direction to UP
                    if event.key == pygame.K_DOWN:  # If DOWN is pressed
                        snake.x_dir = 0  # Set horizontal direction to 0
                        snake.y_dir = 1  # Set vertical direction to DOWN
                
                if snake.x_dir == 0:  # If the snake is moving vertically
                    if event.key == pygame.K_LEFT:  # If LEFT is pressed
                        snake.x_dir = -1  # Set horizontal direction to LEFT
                        snake.y_dir = 0  # Set vertical direction to 0
                    if event.key == pygame.K_RIGHT:  # If RIGHT is pressed
                        snake.x_dir = 1  # Set horizontal direction to RIGHT
                        snake.y_dir = 0  # Set vertical direction to 0
                    if event.key == pygame.K_p:  # Press P to pause and save
                        save_user_progress(user_id, level, score)
                        paused = True
                        pause_font = pygame.font.SysFont(None, 50)
                        pause_text = pause_font.render("Game Paused. Press R to resume.", True, (255, 255, 255))
                        display.blit(pause_text, (50, 250))
                        pygame.display.update()

                        # Wait until user presses R to resume
                        while paused:
                            for pevent in pygame.event.get():
                                if pevent.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if pevent.type == pygame.KEYDOWN and pevent.key == pygame.K_r:
                                    paused = False

        # Filling the background with a gradient
        for y in range(500):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / 500,
                background_top[1] + (background_bottom[1] - background_top[1]) * y / 500,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))

        snake.show()  # Displaying the snake on the screen
        snake.update()  # Updating snake's position
        food.show()  # Displaying the food on the screen
        show_score()  # Displaying the player's score
        show_level()  # Displaying the game level

        if snake.check_eaten():  # If the snake eats the food
            food.new_location()  # Setting a new position for the food
            score += random.randint(1, 5)  # Increasing score by a random value
            snake.grow()  # Growing the snake

        if snake.check_level():  # If a new level is reached
            food.new_location()  # Setting a new position for the food
            level += 1  # Increasing the level
            SPEED += 1  # Increasing the snake's speed
            snake.grow()  # Growing the snake
            update_user_level(user_id, level)
        if snake.death():  # If the snake collides with its tail
            score = 0  # Resetting the score
            level = 0  # Resetting the level
            font = pygame.font.SysFont(None, 100)  # Setting up the font for the "Game Over" text
            text = font.render("Game Over!", True, defeat_colour)  # Creating the "Game Over!" text
            display.blit(text, (50, 200))  # Displaying the text on the screen
            pygame.display.update()  # Updating the screen
            time.sleep(3)  # Waiting for 3 seconds before resetting the game
            snake.reset()  # Resetting the snake's state

        if snake.history[0][0] > 500:  # If the snake goes off the right edge
            snake.history[0][0] = 0  # Moving the snake to the left edge

        if snake.history[0][0] < 0:  # If the snake goes off the left edge
            snake.history[0][0] = 500  # Moving the snake to the right edge
            
        if snake.history[0][1] > 500:  # If the snake goes off the bottom edge
            snake.history[0][1] = 0  # Moving the snake to the top edge
        if snake.history[0][1] < 0:  # If the snake goes off the top edge
            snake.history[0][1] = 500  # Moving the snake to the bottom edge

        pygame.display.update()  # Updating the screen
        clock.tick(SPEED)  # Controlling the game speed

gameLoop()  # Starting the game loop 


