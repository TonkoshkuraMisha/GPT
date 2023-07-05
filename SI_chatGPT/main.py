import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Определение размеров экрана
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

# Создание игрового окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Загрузка изображений
player_image = pygame.image.load("player_ship0.png")
enemy_image = pygame.image.load("enemy_ship0.png")
bullet_image = pygame.image.load("bullet0.png")

# Определение размеров игровых объектов
player_width = 50
player_height = 50
enemy_width = 50
enemy_height = 50
bullet_width = 10
bullet_height = 30

# Определение скоростей объектов
player_speed = 3
enemy_speed = 1
bullet_speed = 5

# Определение начальной позиции игрока
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 10

# Создание списка врагов
enemies = []
enemy_count = 5

for i in range(enemy_count):
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
    enemy_y = random.randint(50, 200)
    enemy = [enemy_x, enemy_y]
    enemies.append(enemy)

# Создание списка пуль
bullets = []
bullet_state = "ready"  # "ready" - пуля находится на позиции игрока, "fire" - пуля движется


# Определение функции для отображения игровых объектов
def draw_object(image, x, y):
    screen.blit(image, (x, y))


# Определение функции для столкновений
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    if bullet_x >= enemy_x and bullet_x <= enemy_x + enemy_width and bullet_y >= enemy_y and bullet_y <= enemy_y + enemy_height:
        return True
    return False


# Основной игровой цикл
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_x += player_speed
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])
                bullet_state = "fire"

        # Обработка отпускания клавиш
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Обновление позиции игрока
    if player_x <= 0:
        player_x = 0
    elif player_x >= SCREEN_WIDTH - player_width:
        player_x = SCREEN_WIDTH - player_width

    # Обновление позиций врагов
    for enemy in enemies:
        enemy[0] += enemy_speed

        # Проверка столкновений с игроком
        if enemy[1] + enemy_height > player_y and enemy[0] + enemy_width > player_x and enemy[
            0] < player_x + player_width:
            running = False

        # Проверка столкновений с пулями
        for bullet in bullets:
            if is_collision(enemy[0], enemy[1], bullet[0], bullet[1]):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

        if enemy[0] <= 0 or enemy[0] >= SCREEN_WIDTH - enemy_width:
            enemy_speed *= -1
            for e in enemies:
                e[1] += 50

    # Обновление позиций пуль
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
            bullet_state = "ready"

    # Отображение игровых объектов
    for enemy in enemies:
        draw_object(enemy_image, enemy[0], enemy[1])

    if bullet_state == "fire":
        draw_object(bullet_image, bullet_x, bullet_y)
        bullet_y -= bullet_speed

    draw_object(player_image, player_x, player_y)

    # Обновление экрана
    pygame.display.update()

# Завершение игры
pygame.quit()
sys.exit()
