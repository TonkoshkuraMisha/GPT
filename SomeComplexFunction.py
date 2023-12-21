import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def complex_function(x, y):
    # Пример комплексной функции (здесь используется z = sin(x + yi))
    z = np.sin(x + 1j * y)
    return np.real(z), np.imag(z)


def plot_complex_function(start_x, end_x, step_x, start_y, end_y, step_y):
    # Создание сетки значений x и y
    x_values = np.arange(start_x, end_x, step_x)
    y_values = np.arange(start_y, end_y, step_y)
    X, Y = np.meshgrid(x_values, y_values)

    # Вычисление значений функции для каждой точки сетки
    Z_real, Z_imag = np.vectorize(complex_function)(X, Y)

    # Построение трёхмерного графика
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z_real, cmap='viridis', alpha=0.7, label='Real part')
    ax.plot_surface(X, Y, Z_imag, cmap='plasma', alpha=0.7, label='Imaginary part')

    # Добавление меток и заголовка
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Complex Function Visualization')

    # Добавление легенды
    ax.legend()

    # Отображение графика
    plt.show()


def main():
    # Задаем интервалы и шаги для значений x и y
    start_x, end_x, step_x = -5, 5, 0.1
    start_y, end_y, step_y = -5, 5, 0.1

    # Построение трёхмерного графика комплексной функции
    plot_complex_function(start_x, end_x, step_x, start_y, end_y, step_y)


if __name__ == "__main__":
    main()
