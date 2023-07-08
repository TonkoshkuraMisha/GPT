import random
import numpy as np
import tables_main_and_free
import winning_bet_lines
import paytable1

game_start_deposit = 50
game_current_deposit = game_start_deposit
game_prize = 0
game_spins = 0
total_spins = 10_000_000  # заданное количество спинов
bet = 2.5  # сумма ставки

total_games = 0  # общее количество игр
total_winnings = 0  # общий выигрыш
total_spins_played = 0  # общее количество сыгранных спинов

while total_spins_played < total_spins:
    # Совершаем спин
    game_spins += 1
    total_spins_played += 1

    selected_elements = []

    for row in tables_main_and_free.main_table:
        index = random.randint(0, len(row) - 1)  # выбираем случайный индекс строки
        prev_index = index - 1 if index > 0 else len(row) - 1  # индекс предыдущего элемента
        next_index = index + 1 if index < len(row) - 1 else 0  # индекс следующего элемента
        selected_elements.append(
            [row[prev_index], row[index], row[next_index]])  # добавляем три выбранных элемента в список

    # Транспонируем результат
    selected_elements = np.array(selected_elements).T.tolist()
    # Выводим выбранные элементы
    # for elements in selected_elements:
    #     print(elements)

    elements_set = set(element for row in selected_elements for element in row)
    # print(elements_set)

    spin_coords = []

    for element in elements_set:
        coords = []
        for i, row in enumerate(selected_elements):
            for j, value in enumerate(row):
                if value == element:
                    coords.append((i, j))
        spin_coords.append(coords)
    # Выводим координаты элементов
    # for coords in spin_coords:
    #     print(coords)

    winning_lines_found = []

    for i, spin_line in enumerate(spin_coords):
        for j, winning_line in enumerate(winning_bet_lines.winning_lines):
            if set(spin_line) == set(winning_line):
                winning_lines_found.append((i, j))

    # if winning_lines_found:
    #     print("Найдены выигрышные линии:")
    #     for line in winning_lines_found:
    #         spin_line_index, winning_line_index = line
    #         print("Выигрышная линия {} в spin_coords соответствует выигрышной линии {} в winning_lines".format(
    #             spin_line_index, winning_line_index))
    # else:
    #     print("Нет выигрышных линий.")

    element_counts = {}

    for element in elements_set:
        count = sum(row.count(element) for row in selected_elements)
        element_counts[element] = count

    win_condition = 0
    for element, count in element_counts.items():
        if element in paytable1.paytable and count in paytable1.paytable[element]:
            if type(paytable1.paytable[element][count]) == float:
                win_condition += paytable1.paytable[element][count]
            elif type(paytable1.paytable[element][count]) == int:
                win_condition += paytable1.paytable[element][count]
            else:
                pass

    # Проверяем, выиграл ли игрок
    if win_condition:
        prize = win_condition  # calculate_prize()  # функция для расчета выигрыша
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
expected_value = round((game_start_deposit * total_games + total_winnings) / (total_spins_played * bet), 8)

# Выводим результат
print("Игра окончена")
print("Общее количество игр:", total_games)
print("Общее количество спинов:", total_spins_played)
print("Общий выигрыш:", total_winnings)
print("Математическое ожидание:", expected_value)
