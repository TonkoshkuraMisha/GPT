workers = {
    'employer1': {'name': 'Jhon', 'salary': 7500},
    'employer2': {'name': 'Emma', 'salary': 8000},
    'employer3': {'name': 'Brad', 'salary': 500}
}

# Поднимаем зарплату Бреду до 8500
workers['employer3']['salary'] = 8500

# Выводим измененный словарь workers
print(workers)
