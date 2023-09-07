import random

matrix = []

for _ in range(3):
    row = []
    for _ in range(5):
        element = random.randint(1, 12)
        row.append(element)
    matrix.append(row)

# Вывод сгенерированной матрицы
for row in matrix:
    print(row)


element_coordinates = {}

# Обход элементов матрицы
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        element = matrix[i][j]
        if element in element_coordinates:
            element_coordinates[element].append((i, j))
        else:
            element_coordinates[element] = [(i, j)]

# Вывод словаря с координатами элементов, отсортированными по возрастанию элементов
for element, coordinates in sorted(element_coordinates.items()):
    print("Элемент:", element)
    print("Координаты:", coordinates)
    print()
