import itertools

symbols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Список всех символов
grid_size = (3, 5)  # Размер игрового поля

combinations = itertools.product(symbols, repeat=grid_size[0] * grid_size[1])

# Открытие файла для записи
with open('combinations.txt', 'w') as file:
    for combination in combinations:
        # Преобразование комбинации в двумерный массив 3x5
        grid = [list(combination[i:i + grid_size[1]]) for i in range(0, grid_size[0] * grid_size[1], grid_size[1])]

        # Запись комбинации в файл
        for row in grid:
            formatted_row = [str(symbol).rjust(2) for symbol in row]
            file.write(' '.join(formatted_row) + '\n')
        file.write('\n')  # Добавление пустой строки между комбинациями
