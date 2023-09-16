import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 1]]
]
SHAPE_COLORS = [(0, 255, 255), (255, 255, 0), (128, 0, 128),
                (0, 128, 0), (255, 0, 0), (0, 0, 255), (255, 165, 0)]

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Initialize fonts
font = pygame.font.Font(None, 36)


# Function to create a new Tetromino
def new_tetromino():
    shape = random.choice(SHAPES)
    color = random.choice(SHAPE_COLORS)
    tetromino = {
        "shape": shape,
        "color": color,
        "x": GRID_WIDTH // 2 - len(shape[0]) // 2,
        "y": 0
    }
    return tetromino


# Function to draw the game grid
def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)


# Function to draw a Tetromino
def draw_tetromino(tetromino):
    for y, row in enumerate(tetromino["shape"]):
        for x, cell in enumerate(row):
            if cell:
                rect = pygame.Rect(
                    (tetromino["x"] + x) * GRID_SIZE,
                    (tetromino["y"] + y) * GRID_SIZE,
                    GRID_SIZE, GRID_SIZE
                )
                pygame.draw.rect(screen, tetromino["color"], rect)
                pygame.draw.rect(screen, BLACK, rect, 2)


# Function to check if a move is valid
def is_valid_move(tetromino, grid):
    for y, row in enumerate(tetromino["shape"]):
        for x, cell in enumerate(row):
            if cell:
                grid_x = tetromino["x"] + x
                grid_y = tetromino["y"] + y
                if (
                        grid_x < 0
                        or grid_x >= GRID_WIDTH
                        or grid_y >= GRID_HEIGHT
                        or grid[grid_y][grid_x]
                ):
                    return False
    return True


# Function to place a Tetromino on the grid
def place_tetromino(tetromino, grid):
    for y, row in enumerate(tetromino["shape"]):
        for x, cell in enumerate(row):
            if cell:
                grid_x = tetromino["x"] + x
                grid_y = tetromino["y"] + y
                grid[grid_y][grid_x] = tetromino["color"]


# Function to check for completed lines and clear them
def check_lines(grid):
    completed_lines = []
    for y, row in enumerate(grid):
        if all(row):
            completed_lines.append(y)
    for y in completed_lines:
        del grid[y]
        grid.insert(0, [0] * GRID_WIDTH)


# Initialize game variables
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
current_tetromino = new_tetromino()
score = 0

# Clock to control game speed
clock = pygame.time.Clock()
fall_speed = 1  # Increase this value to make Tetrominos fall faster

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_tetromino["x"] -= 1
                if not is_valid_move(current_tetromino, grid):
                    current_tetromino["x"] += 1
            elif event.key == pygame.K_RIGHT:
                current_tetromino["x"] += 1
                if not is_valid_move(current_tetromino, grid):
                    current_tetromino["x"] -= 1
            elif event.key == pygame.K_DOWN:
                current_tetromino["y"] += 1
                if not is_valid_move(current_tetromino, grid):
                    current_tetromino["y"] -= 1
            elif event.key == pygame.K_UP:
                rotated = {"shape": list(zip(*reversed(current_tetromino["shape"]))),
                           "color": current_tetromino["color"],
                           "x": current_tetromino["x"],
                           "y": current_tetromino["y"]}
                if is_valid_move(rotated, grid):
                    current_tetromino = rotated

    # Move the Tetromino down
    current_tetromino["y"] += 1
    if not is_valid_move(current_tetromino, grid):
        current_tetromino["y"] -= 1
        place_tetromino(current_tetromino, grid)
        check_lines(grid)
        current_tetromino = new_tetromino()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the game grid and Tetromino
    draw_grid()
    draw_tetromino(current_tetromino)

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(fall_speed)

pygame.quit()
