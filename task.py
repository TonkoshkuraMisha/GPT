# Считываем список целых чисел из входной строки
input_list = list(map(int, input().split()))

# Создаем начальный словарь с последним элементом списка
result_dict = {input_list[-2]: input_list[-1]}

# Обрабатываем остальные элементы списка в обратном порядке
for i in range(len(input_list) - 3, -1, -1):
    result_dict = {input_list[i]: result_dict}

# Выводим полученный словарь
print(result_dict)


def list_to_nested_dict(lst):
    if len(lst) == 2:
        return {lst[0]: lst[1]}
    else:
        return {lst[0]: list_to_nested_dict(lst[1:])}


# Считываем список целых чисел из входной строки
input_list = list(map(int, input().split()))

# Преобразуем список во вложенный словарь с помощью рекурсивной функции
result_dict = list_to_nested_dict(input_list)

# Выводим полученный словарь
print(result_dict)
