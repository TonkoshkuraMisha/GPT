import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define the characters to be used in the Matrix screensaver
MATRIX_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]{}|;:,.<>?'

# Character class
class MatrixCharacter:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.char = random.choice(MATRIX_CHARS)
        self.color = GREEN

    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.char = random.choice(MATRIX_CHARS)

    def draw(self, screen):
        font = pygame.font.SysFont(None, 30)
        text = font.render(self.char, True, self.color)
        screen.blit(text, (self.x, self.y))


# Main function
def main():
    # Initialize the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Matrix Screensaver")

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Create a list to hold Matrix characters
    matrix_characters = [MatrixCharacter(x=random.randint(0, SCREEN_WIDTH),
                                          y=random.randint(0, SCREEN_HEIGHT),
                                          speed=random.randint(1, 3))
                         for _ in range(200)]

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update
        for char in matrix_characters:
            char.update()

        # Render
        screen.fill(BLACK)
        for char in matrix_characters:
            char.draw(screen)

        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)


if __name__ == "__main__":
    main()
