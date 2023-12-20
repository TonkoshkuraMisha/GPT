import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600

# Цвета
black = (0, 0, 0)
green = (0, 255, 0)

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Серпинский треугольник")


# Функция для рисования треугольника Серпинского
def draw_sierpinski(x, y, size, depth):
    if depth == 0:
        # Рисование треугольника
        pygame.draw.polygon(screen, green, [(x, y), (x + size, y), (x + size / 2, y - size)])
    else:
        # Рекурсивное разбиение треугольника на три подтреугольника
        draw_sierpinski(x, y, size / 2, depth - 1)
        draw_sierpinski(x + size / 2, y, size / 2, depth - 1)
        draw_sierpinski(x + size / 4, y + size / 2, size / 2, depth - 1)


# Основной цикл программы
def main():
    depth = 10  # Глубина рекурсии

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Очистка экрана
        screen.fill(black)

        # Рассчитываем начальные координаты для центрирования треугольника
        x = (width - width / 2) / 2
        y = height / 2 - height / 4  # Коррекция для центрирования по вертикали

        # Рисование треугольника Серпинского
        draw_sierpinski(x, y, width / 2, depth)

        # Обновление экрана
        pygame.display.flip()


if __name__ == "__main__":
    main()
