import pygame
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
PASTEL_GREEN = (170, 255, 204)
PASTEL_DARK_GREEN = (0, 102, 51)
LIGHT_GREEN = (144, 238, 144)
PASTEL_RED = (255, 102, 102)
BLACK = (0, 0, 0)

pygame.mixer.music.load("snake_src/arcade_music.mp3")
eat_sound = pygame.mixer.Sound("snake_src/eat_sound.wav")
game_over_sound = pygame.mixer.Sound("snake_src/game_over_sound.wav")

life = 3
score = 0
record = 0
extra_life = 0


class Snake:
    def __init__(self, grid):
        self.grid = grid
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow_pending = 0

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)

        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending += 1

    def check_collision(self):
        head = self.body[0]
        return (
                head in self.body[1:] or
                head[0] < 0 or head[0] >= GRID_WIDTH or
                head[1] < 0 or head[1] >= GRID_HEIGHT
        )

    def draw(self, surface):
        for segment in self.body:
            x, y = segment[0] * GRID_SIZE, segment[1] * GRID_SIZE
            pygame.draw.rect(surface, LIGHT_GREEN, (x, y, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, BLACK, (x, y, GRID_SIZE, GRID_SIZE), 1)  # Отрисовка границ


class Apple:
    def __init__(self, grid):
        self.grid = grid
        self.position = self.random_position()

    def random_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

    def draw(self, surface):
        x, y = self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE
        pygame.draw.rect(surface, PASTEL_RED, (x, y, GRID_SIZE, GRID_SIZE))


def initialize_grid():
    return [[0] * GRID_HEIGHT for _ in range(GRID_WIDTH)]


def update_record(score):
    global record
    if score > record:
        record = score


def update_grid(snake):
    for col in range(GRID_WIDTH):
        for row in range(GRID_HEIGHT):
            snake.grid[col][row] = 0

    for segment in snake.body:
        col, row = segment[0], segment[1]
        if 0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT:
            snake.grid[col][row] = 1


def draw_grid(surface, grid):
    for col in range(GRID_WIDTH):
        for row in range(GRID_HEIGHT):
            x, y = col * GRID_SIZE, row * GRID_SIZE
            pygame.draw.rect(surface, BLACK, (x, y, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, PASTEL_DARK_GREEN, (x + 1, y + 1, GRID_SIZE - 2, GRID_SIZE - 2))


screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("Змейка")

grid = initialize_grid()
snake = Snake(grid)
apple = Apple(grid)

snake_timer = pygame.time.Clock()

pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, 1):
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                snake.direction = (1, 0)

    snake.move()
    update_grid(snake)

    if snake.body[0] == apple.position:
        snake.grow()
        apple.position = apple.random_position()
        score += 1
        update_record(score)
        eat_sound.play()

        if score % 100 == 0:
            extra_life += 1
            life += 1

    if snake.check_collision():
        game_over_sound.play()
        if life > 0:
            life -= 1
            pygame.time.delay(1000)
            snake = Snake(grid)  # Новая змейка
        if life <= 0:
            pygame.mixer.music.stop()
            time.sleep(2)  # Пауза после проигрыша последней жизни
            life = 3
            score = 0
            extra_life = 0
            grid = initialize_grid()
            snake = Snake(grid)
            apple = Apple(grid)
            pygame.mixer.music.play(-1)

    if len(snake.body) < 10:
        snake_timer.tick(8)
    elif 10 <= len(snake.body) < 20:
        snake_timer.tick(10)
    elif 20 <= len(snake.body) < 30:
        snake_timer.tick(12)
    else:
        snake_timer.tick(15)

    screen.fill((PASTEL_GREEN[0], PASTEL_GREEN[1], PASTEL_GREEN[2], 128))
    draw_grid(screen, grid)
    snake.draw(screen)
    apple.draw(screen)

    font = pygame.font.Font("snake_src/orbitron/Orbitron-Bold.ttf", 24)
    score_text = font.render(f"Score: {score}", True, (255, 255, 0, 128))
    record_text = font.render(f"Record: {record}", True, (255, 255, 0, 128))
    lives_text = font.render(f"Life: {life}", True, (255, 255, 0, 128))
    screen.blit(score_text, (WIDTH - 160, 30))
    screen.blit(record_text, (WIDTH - 160, 60))
    screen.blit(lives_text, (WIDTH - 160, 90))

    for i in range(life + extra_life):
        pygame.draw.rect(screen, PASTEL_RED + (8,), (WIDTH - 160 + i * 30, 120, 20, 20))  # Отрисовка сердец

    for i in range(extra_life):
        pygame.draw.rect(screen, PASTEL_RED + (8,),
                         (WIDTH - 160 + (life + i) * 30, 120, 20, 20))  # Дополнительные сердца

    pygame.display.flip()
    for i in range(len(snake.body)):
        x, y = snake.body[i][0] * GRID_SIZE, snake.body[i][1] * GRID_SIZE
        pygame.draw.rect(screen, LIGHT_GREEN, (x, y, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, BLACK, (x, y, GRID_SIZE, GRID_SIZE), 1)  # Отрисовка границ тела змейки

    if life <= 0:
        font = pygame.font.Font("snake_src/arcade_font.ttf", 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0, 128))  # Красный цвет
        screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2 - 36))

        font = pygame.font.Font("snake_src/arcade_font.ttf", 36)
        play_again_text = font.render("Play Again", True, (255, 255, 255, 128))  # Белый цвет
        pygame.draw.rect(screen, (0, 0, 0, 128), (WIDTH // 2 - 90, HEIGHT // 2 + 50, 180, 40))
        screen.blit(play_again_text, (WIDTH // 2 - 80, HEIGHT // 2 + 56))

        pygame.display.flip()

        pygame.time.delay(2000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH // 2 - 90 <= event.pos[0] <= WIDTH // 2 + 90 and HEIGHT // 2 + 50 <= event.pos[
                    1] <= HEIGHT // 2 + 90:
                    life = 3
                    score = 0
                    extra_life = 0
                    grid = initialize_grid()
                    snake = Snake(grid)
                    apple = Apple(grid)
                    pygame.mixer.music.play(-1)

    pygame.display.flip()
