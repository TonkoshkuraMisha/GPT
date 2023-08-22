import random
import numpy as np
import tables_main_and_free
import winning_bet_lines
import paytable_num

game_start_deposit = 50
game_current_deposit = game_start_deposit
game_prize = 0
game_spins = 0
total_spins = 1_000_000  # заданное количество спинов
bet = 2.5  # сумма ставки
total_games = 0  # общее количество игр
total_winnings = 0  # общий выигрыш
total_spins_played = 0  # общее количество сыгранных спинов
element_total_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
elements_total_count2 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
elements_total_count3 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
elements_total_count4 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
elements_total_count5 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
elements_total_count_more = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
while total_spins_played < total_spins:
    # Совершаем спин
    game_spins += 1
    total_spins_played += 1

    selected_elements = []

    for row in tables_main_and_free.free_table:
        index = random.choice(range(len(row)))
        prev_index = (index - 1) % len(row)
        next_index = (index + 1) % len(row)
        selected_elements.append([row[prev_index], row[index], row[next_index]])

    # Транспонируем результат
    selected_elements = np.array(selected_elements).T.tolist()
    elements_set = set(element for row in selected_elements for element in row)
    spin_coords = []

    for element in elements_set:
        coords = []
        for i, row in enumerate(selected_elements):
            for j, value in enumerate(row):
                if value == element:
                    coords.append((i, j))
        spin_coords.append(coords)
    winning_lines_found = []

    for i, spin_line in enumerate(spin_coords):
        for j, winning_line in enumerate(winning_bet_lines.winning_lines):
            if set(spin_line) == set(winning_line):
                winning_lines_found.append((i, j))

    element_counts = {}

    for element in elements_set:
        count = sum(row.count(element) for row in selected_elements)
        element_counts[element] = count

    for element, count in element_counts.items():
        if count == 1:
            element_total_count[element] += 1
        elif count == 2:
            elements_total_count2[element] += 1
        elif count == 3:
            elements_total_count3[element] += 1
        elif count == 4:
            elements_total_count4[element] += 1
        elif count == 5:
            elements_total_count5[element] += 1
        else:
            elements_total_count_more[element] += 1
    win_condition = 0

    for element, count in element_counts.items():
        if element in paytable_num.paytable and count in paytable_num.paytable[element]:
            if type(paytable_num.paytable[element][count]) == float:
                win_condition += paytable_num.paytable[element][count]
            elif type(paytable_num.paytable[element][count]) == int:
                win_condition += paytable_num.paytable[element][count]
            else:
                pass

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
# Вывод общего частотного анализа
print("Общий частотный анализ игры free:")
for symbol, total_count in element_total_count.items():
    print(f"Символ '{symbol}'*1: {total_count}")
print('*' * 100)
for symbol, total_count in elements_total_count2.items():
    print(f"Символ '{symbol}'*2: {total_count}")
print('*' * 100)
for symbol, total_count in elements_total_count3.items():
    print(f"Символ '{symbol}'*3: {total_count}")
print('*' * 100)
for symbol, total_count in elements_total_count4.items():
    print(f"Символ '{symbol}'*4: {total_count}")
print('*' * 100)
for symbol, total_count in elements_total_count5.items():
    print(f"Символ '{symbol}'*5: {total_count}")
print('*' * 100)
for symbol, total_count in elements_total_count_more.items():
    print(f"Символ '{symbol}'*more_than_5: {total_count}")
