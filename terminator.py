# Импортируем модуль для отображения изображений
from PIL import Image

# Создаем изображение с белым фоном
width, height = 100, 150
image = Image.new("RGB", (width, height), "white")
pixels = image.load()

# Определяем цвета для черной и серой краски
black = (0, 0, 0)
gray = (128, 128, 128)

# Определяем пиксели для рисунка Терминатора
terminator_pixels = [
    "                   ",
    "                   ",
    "                   ",
    "                   ",
    "                   ",
    "      xx  xx       ",
    "      xx  xx       ",
    "        xxx        ",
    "        xxx        ",
    "       xxxx        ",
    "                   ",
    "   xx        xx    ",
    "                   ",
    "        xx         ",
    "                   ",
    "   x           x   ",
]

# Размеры пикселей
pixel_width = width // len(terminator_pixels[0])
pixel_height = height // len(terminator_pixels)

# Заполняем изображение
for y, line in enumerate(terminator_pixels):
    for x, char in enumerate(line):
        if char == "x":
            for i in range(pixel_width):
                for j in range(pixel_height):
                    pixels[x * pixel_width + i, y * pixel_height + j] = black
        else:
            for i in range(pixel_width):
                for j in range(pixel_height):
                    pixels[x * pixel_width + i, y * pixel_height + j] = gray

# Сохраняем изображение
image.save("terminator.png")
