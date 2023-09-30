import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
DINO_WIDTH = 50
DINO_HEIGHT = 50
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 50
GROUND_HEIGHT = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game")

# Load Dino image
dino_image = pygame.image.load("dino.png")
dino_image = pygame.transform.scale(dino_image, (DINO_WIDTH, DINO_HEIGHT))

# Load obstacle image
obstacle_image = pygame.image.load("obstacle.png")
obstacle_image = pygame.transform.scale(obstacle_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

# Create Dino object
dino_x = 50
dino_y = SCREEN_HEIGHT - GROUND_HEIGHT - DINO_HEIGHT
dino_speed = 5
jumping = False
jump_count = 10

# Create Obstacle object
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - GROUND_HEIGHT - OBSTACLE_HEIGHT
obstacle_speed = 5

# Game loop
clock = pygame.time.Clock()
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    obstacle_x -= obstacle_speed
    if obstacle_x < 0:
        obstacle_x = SCREEN_WIDTH
        score += 1

    screen.fill(WHITE)
    screen.blit(dino_image, (dino_x, dino_y))
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)
