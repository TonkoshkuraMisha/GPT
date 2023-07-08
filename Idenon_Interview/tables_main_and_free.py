import random
import numpy as np
import winning_bet_lines
import paytable1

# Таблицы Main и Free
main_table = [
    [10, 7, 13, 12, 2, 9, 7, 10, 5, 8, 11, 7, 1, 9, 4, 12, 8, 6, 11, 3, 9, 12, 4, 1, 3, 8, 10, 2, 6, 9, 5, 13, 10, 3,
     11, 8, 5, 7, 12, 11, 5, 4],
    [4, 7, 13, 8, 10, 3, 12, 6, 11, 2, 9, 5, 10, 1, 9, 7, 12, 6, 11, 8, 4, 6, 12, 10, 8, 2, 9, 11, 5, 8, 10, 7, 3, 12],
    [8, 1, 10, 12, 5, 13, 3, 4, 9, 7, 5, 8, 6, 12, 1, 10, 3, 8, 13, 7, 5, 10, 11, 4, 9, 3, 6, 12, 7, 11, 6, 8, 9, 2, 11,
     7, 10, 9, 2, 6, 11, 4, 12],
    [8, 6, 10, 5, 12, 8, 6, 11, 9, 3, 12, 10, 7, 3, 8, 4, 10, 5, 9, 13, 8, 4, 7, 9, 6, 4, 1, 3, 7, 11, 2, 12, 9, 10, 13,
     11, 2, 12, 1, 7, 11],
    [1, 3, 12, 8, 11, 4, 2, 10, 12, 6, 8, 9, 1, 11, 7, 12, 9, 3, 7, 6, 10, 5, 7, 11, 9, 4, 8, 11, 2, 7, 12, 5, 9, 13,
     10, 11, 4, 8, 9, 13, 7, 5, 10]
]

free_table = [
    [11, 12, 8, 7, 11, 1, 8, 12, 10, 6, 8, 5, 12, 1, 9, 1, 10, 11, 6, 9, 5, 10, 13, 7, 11, 1, 10, 12, 1, 5, 9, 8, 5, 11,
     6, 7, 1, 1, 1, 10, 7, 13, 8, 9],
    [8, 6, 12, 11, 1, 1, 6, 5, 8, 9, 10, 1, 1, 1, 11, 9, 10, 7, 8, 5, 9, 6, 11, 12, 8, 1, 7, 10, 1, 8, 9, 13, 12, 11, 7,
     9, 5, 7, 6, 1, 8, 9, 13, 7],
    [11, 13, 8, 12, 1, 10, 11, 6, 1, 9, 5, 8, 10, 6, 1, 9, 10, 1, 1, 7, 13, 9, 1, 10, 6, 8, 12, 5, 11, 6, 9, 7, 5, 12,
     1, 11, 10, 12, 7, 11, 8, 9],
    [9, 7, 6, 8, 12, 1, 10, 11, 1, 7, 8, 12, 1, 11, 9, 5, 7, 10, 11, 6, 1, 7, 8, 13, 9, 5, 11, 1, 1, 1, 12, 10, 6, 7,
     13, 8, 6, 11, 10, 1, 9, 12, 1],
    [10, 1, 11, 9, 8, 5, 7, 10, 12, 8, 13, 11, 9, 6, 1, 12, 11, 7, 10, 8, 9, 7, 1, 12, 9, 10, 1, 12, 1, 8, 7, 11, 10, 5,
     9, 13, 7, 12, 6, 1, 5, 8]
]
#
# selected_elements = []
#
# for row in main_table:
#     index = random.randint(0, len(row) - 1)  # выбираем случайный индекс строки
#     prev_index = index - 1 if index > 0 else len(row) - 1  # индекс предыдущего элемента
#     next_index = index + 1 if index < len(row) - 1 else 0  # индекс следующего элемента
#     selected_elements.append(
#         [row[prev_index], row[index], row[next_index]])  # добавляем три выбранных элемента в список
#
# # Транспонируем результат
# selected_elements = np.array(selected_elements).T.tolist()
#
# # Выводим выбранные элементы
# # for elements in selected_elements:
# #     print(elements)
#
# elements_set = set(element for row in selected_elements for element in row)
#
# # print(elements_set)
#
# spin_coords = []
#
# for element in elements_set:
#     coords = []
#     for i, row in enumerate(selected_elements):
#         for j, value in enumerate(row):
#             if value == element:
#                 coords.append((i, j))
#     spin_coords.append(coords)
#
# # Выводим координаты элементов
# # for coords in spin_coords:
# #     print(coords)
#
# winning_lines_found = []
#
# for i, spin_line in enumerate(spin_coords):
#     for j, winning_line in enumerate(winning_bet_lines.winning_lines):
#         if set(spin_line) == set(winning_line):
#             winning_lines_found.append((i, j))
#
# # if winning_lines_found:
# #     print("Найдены выигрышные линии:")
# #     for line in winning_lines_found:
# #         spin_line_index, winning_line_index = line
# #         print("Выигрышная линия {} в spin_coords соответствует выигрышной линии {} в winning_lines".format(
# #             spin_line_index, winning_line_index))
# # else:
# #     print("Нет выигрышных линий.")
#
#
# element_counts = {}
#
# for element in elements_set:
#     count = sum(row.count(element) for row in selected_elements)
#     element_counts[element] = count
#
#
# for element, count in element_counts.items():
#     if element in paytable1.paytable and count in paytable1.paytable[element]:
#         print(type(paytable1.paytable[element][count]))
#
