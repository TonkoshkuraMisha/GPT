import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 40
PACMAN_SPEED = 5
GHOST_SPEED = 3
SCORE_FONT = pygame.font.Font(None, 36)
GAME_OVER_FONT = pygame.font.Font(None, 72)

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Load images
pacman = pygame.image.load("pacman.png")
pacman = pygame.transform.scale(pacman, (GRID_SIZE, GRID_SIZE))
ghost = pygame.image.load("ghost.png")
ghost = pygame.transform.scale(ghost, (GRID_SIZE, GRID_SIZE))
pellet = pygame.image.load("pellet.png")
pellet = pygame.transform.scale(pellet, (20, 20))
pellet_radius = 10
maze_image = pygame.image.load("maze.png")

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Game variables
pacman_rect = pacman.get_rect()
pacman_x, pacman_y = 400, 300
pacman_rect.topleft = (pacman_x, pacman_y)
pacman_direction = "stop"
ghosts = []

# Create ghost instances
for _ in range(4):
    ghost_x = random.randint(0, SCREEN_WIDTH - GRID_SIZE)
    ghost_y = random.randint(0, SCREEN_HEIGHT - GRID_SIZE)
    ghost_rect = ghost.get_rect(topleft=(ghost_x, ghost_y))
    ghosts.append(ghost_rect)

# Pellets
pellets = [(100, 100), (200, 100), (300, 100), (400, 100)]  # Example positions
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pacman_direction = "up"
    if keys[pygame.K_DOWN]:
        pacman_direction = "down"
    if keys[pygame.K_LEFT]:
        pacman_direction = "left"
    if keys[pygame.K_RIGHT]:
        pacman_direction = "right"

    # Update Pac-Man's position
    if pacman_direction == "up":
        pacman_y -= PACMAN_SPEED
    if pacman_direction == "down":
        pacman_y += PACMAN_SPEED
    if pacman_direction == "left":
        pacman_x -= PACMAN_SPEED
    if pacman_direction == "right":
        pacman_x += PACMAN_SPEED

    # Boundary checking
    if pacman_x < 0:
        pacman_x = 0
    if pacman_x > SCREEN_WIDTH - GRID_SIZE:
        pacman_x = SCREEN_WIDTH - GRID_SIZE
    if pacman_y < 0:
        pacman_y = 0
    if pacman_y > SCREEN_HEIGHT - GRID_SIZE:
        pacman_y = SCREEN_HEIGHT - GRID_SIZE

    # Check for collisions with pellets
    eaten_pellets = [p for p in pellets if pacman_rect.colliderect(pellet.get_rect(topleft=p))]
    for pellet_pos in eaten_pellets:
        score += 10
        pellets.remove(pellet_pos)

    # Check for collisions with ghosts
    for ghost_rect in ghosts:
        if pacman_rect.colliderect(ghost_rect):
            game_over_text = GAME_OVER_FONT.render("Game Over", True, RED)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(game_over_text, game_over_rect)
            pygame.display.update()
            pygame.time.delay(2000)  # Show "Game Over" for 2 seconds
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the maze
    screen.blit(maze_image, (0, 0))

    # Draw pellets
    for pellet_pos in pellets:
        screen.blit(pellet, pellet_pos)

    # Draw Pac-Man
    screen.blit(pacman, (pacman_x, pacman_y))

    # Draw ghosts
    for ghost_rect in ghosts:
        screen.blit(ghost, ghost_rect.topleft)

    # Display the score
    score_text = SCORE_FONT.render(f"Score: {score}", True, YELLOW)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
sys.exit()
