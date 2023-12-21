import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from mpmath import zeta, im, re


def riemann_zeta_function(sigma, t):
    # Вычисление значения Дзета-функции Римана для заданных sigma и t
    s = sigma + 1j * t
    return np.abs(zeta(s))


def plot_riemann_zeta_function(sigma_range, t_range, num_points=100):
    # Создание сетки значений sigma и t
    sigma_values = np.linspace(sigma_range[0], sigma_range[1], num_points)
    t_values = np.linspace(t_range[0], t_range[1], num_points)
    Sigma, T = np.meshgrid(sigma_values, t_values)

    # Вычисление значений Дзета-функции Римана для каждой точки сетки
    Z_values = np.vectorize(riemann_zeta_function)(Sigma, T)

    # Построение трехмерного графика
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(Sigma, T, Z_values, cmap='viridis', alpha=0.7)

    # Добавление меток и заголовка
    ax.set_xlabel('σ')
    ax.set_ylabel('t')
    ax.set_zlabel('|ζ(σ + it)|')
    ax.set_title('Riemann Zeta Function Visualization')

    # Отображение графика
    plt.show()


def main():
    # Задаем интервалы для sigma и t
    sigma_range = [-5, 20]
    t_range = [-5, 5]

    # Построение трехмерного графика Дзета-функции Римана
    plot_riemann_zeta_function(sigma_range, t_range)


if __name__ == "__main__":
    main()
