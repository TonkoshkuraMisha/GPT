import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Определяем символы, которые будут использованы в скринсейвере Matrix
MATRIX_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]{}|;:,.<>?'


# Класс символа
class MatrixCharacter:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.char = random.choice(MATRIX_CHARS)
        self.color = GREEN

    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.char = random.choice(MATRIX_CHARS)
            self.speed = random.randint(5, 10)  # Увеличиваем скорость для каждого символа

    def draw(self, screen):
        font = pygame.font.SysFont(None, 30)
        text = font.render(self.char, True, self.color)
        screen.blit(text, (self.x, self.y))


# Основная функция
def main():
    # Инициализация экрана
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Matrix Screensaver")

    # Часы для управления частотой кадров
    clock = pygame.time.Clock()

    # Создаем список символов Matrix
    matrix_characters = [MatrixCharacter(x=random.randint(0, SCREEN_WIDTH),
                                         y=random.randint(-SCREEN_HEIGHT, 0),  # Располагаем символы выше экрана
                                         speed=random.randint(5, 10))  # Случайная скорость для каждого символа
                         for _ in range(2000)]  # Больше символов

    # Основной цикл
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Обновление
        for char in matrix_characters:
            char.update()

        # Отрисовка
        screen.fill(BLACK)
        for char in matrix_characters:
            char.draw(screen)

        pygame.display.flip()

        # Ограничение частоты кадров
        clock.tick(60)


if __name__ == "__main__":
    main()
