import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание окна
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Инициализация платформ и мяча
player_paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 20, 100, 10)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        player_paddle.x += PADDLE_SPEED

    # Движение мяча
    ball.x += ball_dx
    ball.y += ball_dy

    # Отскок мяча от стен
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx

    # Отскок мяча от верхней границы
    if ball.top <= 0:
        ball_dy = -ball_dy

    # Проверка столкновения мяча с платформой
    if ball.colliderect(player_paddle) and ball_dy > 0:
        ball_dy = -ball_dy

    # Проверка завершения игры (мяч вылетел за нижнюю границу)
    if ball.top >= HEIGHT:
        running = False

    # Отрисовка игровых объектов
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, player_paddle)
    pygame.draw.ellipse(window, WHITE, ball)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты обновления
    pygame.time.delay(30)

# Завершение игры
pygame.quit()
