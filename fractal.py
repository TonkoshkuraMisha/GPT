import matplotlib.pyplot as plt
import numpy as np


def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, max_iter):
    """Функция, рисующая фрактал Мандельброта."""
    x, y = np.meshgrid(np.linspace(xmin, xmax, xn), np.linspace(ymin, ymax, yn))
    c = x + y * 1j
    z = c
    fractal = np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        z = z ** 2 + c
        mask = (fractal == 0) & (abs(z) > 2)
        fractal[mask] = i
        z[mask] = 0

    return fractal


# Рисование фрактала Мандельброта
fractal = mandelbrot_set(-2.5, 1.5, -2, 2, 1000, 1000, 100)
plt.imshow(fractal, cmap='viridis')
plt.axis('off')
plt.show()
