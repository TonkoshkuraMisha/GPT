import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# Класс змейки
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)

    def grow(self):
        self.body.append((0, 0))  # Новый сегмент змейки

    def check_collision(self):
        head = self.body[0]
        return (
                head in self.body[1:] or
                head[0] < 0 or head[0] >= GRID_WIDTH or
                head[1] < 0 or head[1] >= GRID_HEIGHT
        )

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (*segment, GRID_SIZE, GRID_SIZE))


# Класс яблока
class Apple:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (*self.position, GRID_SIZE, GRID_SIZE))


# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Создание змейки и яблока
snake = Snake()
apple = Apple()

# Таймер для движения змейки
snake_timer = pygame.time.Clock()

# Главный цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT

    # Движение змейки
    snake.move()

    # Проверка столкновения с яблоком
    if snake.body[0] == apple.position:
        snake.grow()
        apple.position = apple.random_position()

    # Проверка столкновения со стенами или самой собой
    if snake.check_collision():
        pygame.quit()
        sys.exit()

    # Отрисовка на экране
    screen.fill(BLACK)
    snake.draw(screen)
    apple.draw(screen)

    pygame.display.flip()

    # Задержка для контроля скорости
    snake_timer.tick(10)
