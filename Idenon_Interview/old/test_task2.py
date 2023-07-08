import random


def generate_random_combination(symbols, grid_size):
    return [random.choice(symbols) for _ in range(grid_size[0] * grid_size[1])]


def is_winning_combination(combination, paytable):
    return combination in paytable


def get_winning_coefficient(combination, paytable):
    return paytable[combination]


def monte_carlo_simulation(symbols, grid_size, paytable, num_simulations):
    total_winnings = 0

    for _ in range(num_simulations):
        combination = generate_random_combination(symbols, grid_size)

        if is_winning_combination(combination, paytable):
            coefficient = get_winning_coefficient(combination, paytable)
            total_winnings += coefficient

    average_winnings = total_winnings / num_simulations

    return average_winnings


# Пример использования
symbols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
grid_size = (3, 5)
paytable = {
    (1, 1, 1): 10,
    (2, 2, 2): 20,
    # ...
}
num_simulations = 100000

average_winnings = monte_carlo_simulation(symbols, grid_size, paytable, num_simulations)
print(f"Приближенное математическое ожидание: {average_winnings}")
