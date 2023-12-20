import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 800

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Зелёный фрактал Мандельброта")

# Определение области отображения
x_min, x_max = -2, 2
y_min, y_max = -2, 2

# Максимальное количество итераций для определения цвета
max_iterations = 100

# Цвета
background_color = (0, 0, 0)
green_palette = [(0, i, 0) for i in range(256)]  # Градиент от черного к зелёному


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z * z + c
        n += 1
    if n == max_iterations:
        return 0  # Черный для точек в множестве Мандельброта
    else:
        return n


# Основной цикл программы
def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Очистка экрана
        screen.fill(background_color)

        # Рисование фрактала Мандельброта
        for x in range(width):
            for y in range(height):
                # Маппинг координат на область отображения
                real = x * (x_max - x_min) / (width - 1) + x_min
                imag = y * (y_max - y_min) / (height - 1) + y_min

                c = complex(real, imag)
                color_value = mandelbrot(c)

                # Определение цвета на основе количества итераций
                color = green_palette[color_value % 256]

                # Отображение пикселя
                screen.set_at((x, y), color)

        # Обновление экрана
        pygame.display.flip()

        # Установка FPS
        clock.tick(30)


if __name__ == "__main__":
    main()
