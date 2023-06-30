import pygame
import numpy as np

# Define constants
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 10
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create the game grid
grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=int)

# Set up the initial state of the game grid
# Ex1.
# grid[1:4, 1:4] = [[0, 1, 0],
#                   [0, 0, 1],
#                   [1, 1, 1]]
# Ex2. pattern called the "pulsar"
# grid[6:9, 4:7] = [[0, 1, 1],
#                   [1, 0, 1],
#                   [0, 0, 0]]
# grid[6:9, 9:12] = [[0, 1, 1],
#                    [1, 0, 1],
#                    [0, 0, 0]]
# grid[4:7, 6:9] = [[0, 1, 0],
#                   [0, 0, 1],
#                   [1, 1, 0]]
# grid[9:12, 6:9] = [[0, 1, 0],
#                    [0, 0, 1],
#                    [1, 1, 0]]
# Ex3. cell pattern called the "glider gun"
grid[1:4, 1:4] = [[0, 1, 0],
                  [0, 0, 1],
                  [1, 1, 1]]
grid[10:14, 1:4] = [[1, 0, 0],
                    [1, 1, 0],
                    [0, 1, 1],
                    [0, 0, 1]]
grid[11:13, 11:13] = [[0, 1],
                      [1, 0]]

grid[14:17, 4:7] = [[0, 0, 0],
                    [0, 1, 1],
                    [1, 1, 0]]
grid[15:17, 8:10] = [[1, 0],
                     [1, 1]]
grid[16:19, 11:14] = [[0, 0, 1],
                      [0, 1, 0],
                      [1, 0, 0]]
grid[19:21, 5:7] = [[1, 0],
                    [1, 1]]
grid[20:22, 10:12] = [[1, 1],
                      [1, 0]]

grid[21:24, 3:6] = [[0, 0, 1],
                    [1, 0, 1],
                    [0, 1, 1]]
grid[22:24, 8:10] = [[1, 1],
                     [1, 0]]
grid[24:26, 6:8] = [[1, 1],
                    [1, 1]]
grid[24:27, 18:20] = [[1, 1],
                      [1, 0],
                      [1, 1]]
grid[25:27, 17:19] = [[1, 1],
                      [1, 1]]

grid[26:29, 15:17] = [[0, 1],
                      [1, 0],
                      [0, 0]]
grid[26:28, 24:26] = [[1, 0],
                      [0, 1]]

grid[28:30, 16:18] = [[1, 1],
                      [1, 0]]
grid[29:31, 22:24] = [[0, 1],
                      [1, 0]]

grid[30:33, 17:20] = [[1, 0, 1],
                      [0, 1, 0],
                      [1, 0, 1]]

# Define functions for updating the game grid
def count_neighbors(x, y):
    return np.sum(grid[x - 1:x + 2, y - 1:y + 2]) - grid[x, y]


def update_grid():
    global grid
    new_grid = np.copy(grid)
    for x in range(1, GRID_WIDTH - 1):
        for y in range(1, GRID_HEIGHT - 1):
            num_neighbors = count_neighbors(x, y)
            if grid[x, y] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                new_grid[x, y] = 0
            elif grid[x, y] == 0 and num_neighbors == 3:
                new_grid[x, y] = 1
    grid = new_grid


# Define the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game grid
    update_grid()

    # Draw the game grid
    screen.fill(BLACK)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x, y] == 1:
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, WHITE, rect)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Clean up
pygame.quit()
