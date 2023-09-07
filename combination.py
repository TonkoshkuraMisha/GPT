from itertools import product


def combinations_with_replacement_generator(tuple_values, length):
    unique_combinations = set(product(tuple_values, repeat=length))
    yield from unique_combinations


symbol = '@'
# Создание генератора комбинаций с повторениями
combinations_generator_2 = combinations_with_replacement_generator((1, symbol), 2)
combinations_generator_3 = combinations_with_replacement_generator((1, symbol, symbol), 3)
combinations_generator_4 = combinations_with_replacement_generator((1, symbol, symbol, symbol), 4)
combinations_generator_5 = combinations_with_replacement_generator((1, symbol, symbol, symbol, symbol), 5)

# Итерация по всем уникальным комбинациям
for combination in combinations_generator_2:
    print(combination)

# Итерация по всем уникальным комбинациям
for combination in combinations_generator_3:
    print(combination)

# Итерация по всем уникальным комбинациям
for combination in combinations_generator_4:
    print(combination)

# Итерация по всем уникальным комбинациям
for combination in combinations_generator_5:
    print(combination)
