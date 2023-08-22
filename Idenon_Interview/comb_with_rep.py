from itertools import product


def combinations_with_replacement_generator(tuple_values, length):
    unique_combinations = set(product(tuple_values, repeat=length))
    yield from unique_combinations


all_combinations = []

for symbol in range(2, 13):

    # Создание генератора комбинаций с повторениями
    combinations_generator_2 = combinations_with_replacement_generator((1, symbol), 2)
    combinations_generator_3 = combinations_with_replacement_generator((1, symbol, symbol), 3)
    combinations_generator_4 = combinations_with_replacement_generator((1, symbol, symbol, symbol), 4)
    combinations_generator_5 = combinations_with_replacement_generator((1, symbol, symbol, symbol, symbol), 5)

    # Добавление всех уникальных комбинаций в список
    all_combinations.extend(combinations_generator_2)
    all_combinations.extend(combinations_generator_3)
    all_combinations.extend(combinations_generator_4)
    all_combinations.extend(combinations_generator_5)

# Преобразование списка комбинаций в кортеж
all_combinations_tuple = tuple(all_combinations)

# # Вывод общего количества комбинаций
# print("Общее количество комбинаций:", len(all_combinations_tuple))
#
# # Вывод всех комбинаций
# for combination in all_combinations_tuple:
#     print(combination)
