import random
import numpy as np
import tables_main_and_free
from Idenon_Interview import comb_with_rep

game_start_deposit = 50
game_current_deposit = game_start_deposit
game_prize = 0
game_spins = 0
total_spins = 100000  # заданное количество спинов
bet = 2.5  # сумма ставки
free_spin = 0
total_games = 0  # общее количество игр
total_winnings = 0  # общий выигрыш
total_spins_played = 0  # общее количество сыгранных спинов

while total_spins_played < total_spins:
    # Совершаем спин
    game_spins += 1
    total_spins_played += 1

    selected_elements = []

    for row in (tables_main_and_free.free_table if free_spin else tables_main_and_free.main_table): # Математическое ожидание: 0.6255
    # for row in (tables_main_and_free.main_table): # Математическое ожидание: 0.5217
    # for row in (tables_main_and_free.free_table): # Математическое ожидание: 1.6915
        index = random.choice(range(len(row)))
        prev_index = (index - 1) % len(row)
        next_index = (index + 1) % len(row)
        selected_elements.append([row[prev_index], row[index], row[next_index]])

    # Транспонируем результат
    selected_elements = np.array(selected_elements).T.tolist()
    elements_set = set(element for row in selected_elements for element in row)

    win_condition = 0
    for combination in comb_with_rep.all_combinations_tuple:
        for string in selected_elements:
            if len(combination) == 5 and combination in zip(string, string[1:]):
                win_condition += 50
                print(combination, string)
            elif len(combination) == 4 and combination in zip(string, string[1:]):
                win_condition += 25
                print(combination, string)
            elif len(combination) == 3 and combination in zip(string, string[1:]):
                win_condition += 2.5
                print(combination, string)
            elif len(combination) == 2 and combination in zip(string, string[1:]):
                win_condition += 0.5
                print(combination, string)
            else:
                pass

    element_counts = {}

    for element in elements_set:
        count = sum(row.count(element) for row in selected_elements)
        element_counts[element] = count

    if 13 in element_counts and element_counts[13] > 2:
        if element_counts[13] == 3:
            free_spin += 5
            win_condition += 12.5
        elif element_counts[13] == 4:
            free_spin += 10
            win_condition += 50
        elif element_counts[13] == 5:
            free_spin += 25
            win_condition += 100
    if free_spin:
        free_spin -= 1

    # Проверяем, выиграл ли игрок
    if win_condition:
        prize = win_condition
        game_prize += prize
        game_current_deposit = game_start_deposit + game_prize
        total_winnings += prize
    else:
        game_current_deposit -= bet

    # Проверяем, достигнуто ли общее количество спинов
    if total_spins_played == total_spins:
        # Начинаем новую игру
        total_games += 1
        game_current_deposit = game_start_deposit
        game_prize = 0
        game_spins = 0

# Вычисляем отношение с округлением до десятитысячных
expected_value = round((game_start_deposit * total_games + total_winnings) / (total_spins_played * bet), 4)

# Выводим результат
print("Игра окончена")
print("Общее количество игр:", total_games)
print("Общее количество спинов:", total_spins_played)
print("Общий выигрыш:", total_winnings)
print("Математическое ожидание:", expected_value)
