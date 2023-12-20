import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 800

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ковер Серпинского")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)


def draw_sierpinski_carpet(x, y, size, depth):
    if depth == 0:
        pygame.draw.rect(screen, white, pygame.Rect(x, y, size, size))
    else:
        new_size = size / 3
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    draw_sierpinski_carpet(x + i * new_size, y + j * new_size, new_size, depth - 1)


# Основной цикл программы
def main():
    clock = pygame.time.Clock()

    depth = 4  # Глубина рекурсии

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Очистка экрана
        screen.fill(black)

        # Рисование ковра Серпинского
        draw_sierpinski_carpet(0, 0, width, depth)

        # Обновление экрана
        pygame.display.flip()

        # Установка FPS
        clock.tick(30)


if __name__ == "__main__":
    main()
