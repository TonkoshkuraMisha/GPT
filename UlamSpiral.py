import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 800

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Спираль Улама")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def draw_spiral():
    radius = 1
    angle = 0

    for i in range(10000):
        x = width // 2 + int(radius * math.cos(angle))
        y = height // 2 + int(radius * math.sin(angle))

        cell_size = 50

        grid_x = x // cell_size
        grid_y = y // cell_size

        if is_prime(i):
            font = pygame.font.Font(None, 30)
            text = font.render(str(i), True, green)
            screen.blit(text, (grid_x * cell_size + 10, grid_y * cell_size + 10))

        angle += 0.02
        radius += 0.5


# Основной цикл программы
def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Очистка экрана
        screen.fill(black)

        # Рисование Спирали Улама
        draw_spiral()

        # Обновление экрана
        pygame.display.flip()

        # Установка FPS
        clock.tick(30)


if __name__ == "__main__":
    main()
