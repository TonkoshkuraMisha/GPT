import pygame
import random
import copy

# Set the field size parameters
cell_size = 12
num_rows = 75
num_cols = 120

# Set colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set the maximum number of generations before resetting
max_generations = 1e4


# Initialize the grid with random alive cells
def initialize_grid():
    return [[random.randint(0, 1) for _ in range(num_cols)] for _ in range(num_rows)]


# Count the number of alive neighbors for a given cell
def count_neighbors(grid, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor_row = row + i
            neighbor_col = col + j

            # Check if the neighbor is within the grid boundaries
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                count += grid[neighbor_row][neighbor_col]

    # Subtract the center cell, as we counted it as a neighbor
    count -= grid[row][col]
    return count


# Update the grid based on the rules of the Game of Life
def update_grid(grid):
    new_grid = copy.deepcopy(grid)

    for row in range(num_rows):
        for col in range(num_cols):
            neighbors = count_neighbors(grid, row, col)
            is_cell_alive = grid[row][col]

            # Apply the rules of the Game of Life
            if is_cell_alive and (neighbors < 2 or neighbors > 3):
                new_grid[row][col] = 0  # Cell dies
            elif not is_cell_alive and neighbors == 3:
                new_grid[row][col] = 1  # Cell becomes alive

    return new_grid


# Draw the grid on the Pygame window with a checkered pattern
def draw_grid(screen, grid):
    screen.fill(BLACK)

    for row in range(num_rows):
        for col in range(num_cols):
            x = col * cell_size
            y = row * cell_size

            # Draw thin borders between cells
            pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size), 1)

            color = GREEN if grid[row][col] else BLACK
            pygame.draw.rect(screen, color, (x + 1, y + 1, cell_size - 2, cell_size - 2))


# Main function to run the Game of Life
def main():
    pygame.init()

    # Set up the Pygame window
    screen = pygame.display.set_mode((num_cols * cell_size, num_rows * cell_size))
    pygame.display.set_caption("Conway's Game of Life")

    # Initialize the grid
    grid = initialize_grid()

    clock = pygame.time.Clock()

    generations = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw the grid
        grid = update_grid(grid)
        draw_grid(screen, grid)

        pygame.display.flip()
        clock.tick(4)  # Set the frame rate

        generations += 1

        # Reset the grid if it reaches an equilibrium position
        if generations > max_generations:
            grid = initialize_grid()
            generations = 0

    pygame.quit()


if __name__ == "__main__":
    main()
