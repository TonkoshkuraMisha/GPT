import pygame
import sys
import random
import time

# To-Do List
# 1. Плавное увеличение скорости в процессе набора очков;
# 2. Отображение екстра-жизней и их учёт при достижении определённых условий;
# 3. Полупрозрачность записей и жизней на игровом поле, чтобы не путали игрока;
# 4. Доработать меню старта и рестарта игры.

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


class Snake:
    def __init__(self, grid, initial_speed):
        self.grid = grid
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow_pending = 0
        self.speed = initial_speed
        self.move_timer = 0
        self.move_period = 1.0 / self.speed
        self.acceleration = 0.01

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

    def update_speed(self, dt, score):
        self.move_timer += dt
        if self.move_timer >= self.move_period:
            self.speed += self.acceleration * score
            self.move_period = 1.0 / self.speed
            self.move_timer = 0

    def draw(self, surface):
        for segment in self.body:
            x, y = segment[0] * GRID_SIZE, segment[1] * GRID_SIZE
            pygame.draw.rect(surface, LIGHT_GREEN, (x, y, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, BLACK, (x, y, GRID_SIZE, GRID_SIZE), 1)


class Apple:
    def __init__(self, grid):
        self.grid = grid
        self.position = self.random_position()

    def random_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

    def draw(self, surface):
        x, y = self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE
        pygame.draw.rect(surface, PASTEL_RED, (x, y, GRID_SIZE, GRID_SIZE))


class FlashingApple(Apple):
    def __init__(self, grid):
        super().__init__(grid)
        self.is_flashing = False
        self.flash_timer = 0
        self.flash_period = 1.0
        self.move_timer = 0
        self.move_period = 10

    def update(self, dt):
        self.flash_timer += dt
        if self.flash_timer >= self.flash_period:
            self.is_flashing = not self.is_flashing
            self.flash_timer = 0

        self.move_timer += dt
        if self.move_timer >= self.move_period:
            self.position = self.random_position()
            self.move_timer = 0

    def draw(self, surface):
        if self.is_flashing:
            super().draw(surface)
        else:
            pygame.draw.rect(surface, (255, 0, 0),
                             (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


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


def draw_info(surface, score, record, life):
    font = pygame.font.Font("snake_src/orbitron/Orbitron-Bold.ttf", 24)
    score_text = font.render(f"Score: {score}", True, (255, 255, 0, 128))
    record_text = font.render(f"Record: {record}", True, (255, 255, 0, 128))
    lives_text = font.render(f"Life: {life}", True, (255, 255, 0, 128))
    surface.blit(score_text, (WIDTH - 180, 30))
    surface.blit(record_text, (WIDTH - 180, 60))
    surface.blit(lives_text, (WIDTH - 180, 90))

    for i in range(life):
        pygame.draw.rect(surface, PASTEL_RED + (128,), (WIDTH - 180 + i * 30, 120, 20, 20))


def add_extra_life(score):
    was_added = False
    extra_life = (score // 10)%2
    return extra_life


screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("Змейка")

grid = initialize_grid()
initial_speed = 5
snake = Snake(grid, initial_speed)
apple = Apple(grid)
flashing_apple = FlashingApple(grid)

snake_timer = pygame.time.Clock()

pygame.mixer.music.play(-1)

while True:
    dt = snake_timer.tick(5) / 1000.0

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
    snake.update_speed(dt, score)
    # check_extra_life(score, 0)

    if snake.body[0] == apple.position:
        snake.grow()
        apple.position = apple.random_position()
        score += 1
        update_record(score)
        eat_sound.play()
        life += check_extra_life(score, 0)

    flashing_apple.update(dt)

    if snake.body[0] == flashing_apple.position:
        snake.grow()
        flashing_apple.position = flashing_apple.random_position()
        score += 3
        update_record(score)
        eat_sound.play()
        life += check_extra_life(score, 0)

    if snake.check_collision():
        game_over_sound.play()
        if life >= 0:
            life -= 1
            pygame.time.delay(1000)
            snake = Snake(grid, initial_speed)
        if life < 0:
            pygame.mixer.music.stop()
            time.sleep(2)
            life = 3
            score = 0
            grid = initialize_grid()
            snake = Snake(grid, initial_speed)
            apple = Apple(grid)
            flashing_apple = FlashingApple(grid)

    screen.fill(PASTEL_GREEN)
    draw_grid(screen, grid)
    snake.draw(screen)
    apple.draw(screen)
    flashing_apple.draw(screen)

    # 3. Полупрозрачность записей и жизней на игровом поле
    draw_info(screen, score, record, life)

    pygame.display.flip()

    if life <= 0:
        font = pygame.font.Font("snake_src/arcade_font.ttf", 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2 - 36))

        font = pygame.font.Font("snake_src/arcade_font.ttf", 36)
        play_again_text = font.render("Play Again", True, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 - 90, HEIGHT // 2 + 50, 180, 40), border_radius=10)
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
                    grid = initialize_grid()
                    snake = Snake(grid, initial_speed)
                    apple = Apple(grid)
                    flashing_apple = FlashingApple(grid)
                    pygame.mixer.music.play(-1)
    pygame.display.flip()
