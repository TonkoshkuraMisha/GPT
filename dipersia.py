import random


def calculate_variance(data):
    n = len(data)
    mean = sum(data) / n
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    variance = squared_diff_sum / n
    return variance


# Симулируем бросок двух шестигранных костей 1000 раз
num_simulations = 10_000_000
dice_rolls = [random.randint(1, 6) + random.randint(1, 6) for _ in range(num_simulations)]

variance = calculate_variance(dice_rolls)
print("Вычисленная дисперсия:", variance)
