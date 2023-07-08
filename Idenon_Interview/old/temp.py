from collections import Counter

paytable = {
    'Wild': {
        3: 50,
        2: 10
    },
    'gloves': {
        3: 0,
        2: 0
    },
    'armor': {
        3: 0,
        2: 0
    },
    'first_aid_kit': {
        3: 0,
        2: 0
    },
    'grenade': {
        3: 0,
        2: 0
    },
    'karambit': {
        3: 0,
        2: 0
    },
    'P90': {
        3: 0,
        2: 0
    },
    'shotgun': {
        3: 0,
        2: 0
    },
    'assault_rifle': {
        3: 0,
        2: 0
    },
    'rifle': {
        3: 0,
        2: 0
    },
    'submachine_gun': {
        3: 0,
        2: 0
    },
    'pistol': {
        3: 0,
        2: 0
    },
    't_scat': {
        3: 0,
        2: 0
    }
}

free_paytable = {
    'Wild': {
        3: 100,
        2: 20
    },
    'gloves': {
        3: 30,
        2: 5
    },
    'armor': {
        3: 20,
        2: 4
    },
    'first_aid_kit': {
        3: 15,
        2: 3
    },
    'grenade': {
        3: 10,
        2: 2
    },
    'karambit': {
        3: 8,
        2: 1
    },
    'P90': {
        3: 6,
        2: 1
    },
    'shotgun': {
        3: 5,
        2: 1
    },
    'assault_rifle': {
        3: 4,
        2: 1
    },
    'rifle': {
        3: 3,
        2: 1
    },
    'submachine_gun': {
        3: 2,
        2: 1
    },
    'pistol': {
        3: 2,
        2: 1
    },
    't_scat': {
        3: 0,
        2: 0
    }
}


def calculate_probabilities(data):
    total_combinations = len(data)
    counts = Counter(data)
    probabilities = {combination: count / total_combinations for combination, count in counts.items()}
    return probabilities


# Таблицы Main и Free
main_table = [
    [10, 7, 13, 12, 2, 9, 7, 10, 5, 8, 11, 7, 1, 9, 4, 12, 8, 6, 11, 3, 9, 12, 4, 1, 3, 8, 10, 2, 6, 9, 5, 13, 10, 3,
     11, 8, 5, 7, 12, 11, 5, 4],
    [4, 7, 13, 8, 10, 3, 12, 6, 11, 2, 9, 5, 10, 1, 9, 7, 12, 6, 11, 8, 4, 6, 12, 10, 8, 2, 9, 11, 5, 8, 10, 7, 3, 12],
    [8, 1, 10, 12, 5, 13, 3, 4, 9, 7, 5, 8, 6, 12, 1, 10, 3, 8, 13, 7, 5, 10, 11, 4, 9, 3, 6, 12, 7, 11, 6, 8, 9, 2, 11,
     7, 10, 9, 2, 6, 11, 4, 12],
    [8, 6, 10, 5, 12, 8, 6, 11, 9, 3, 12, 10, 7, 3, 8, 4, 10, 5, 9, 13, 8, 4, 7, 9, 6, 4, 1, 3, 7, 11, 2, 12, 9, 10, 13,
     11, 2, 12, 1, 7, 11],
    [1, 3, 12, 8, 11, 4, 2, 10, 12, 6, 8, 9, 1, 11, 7, 12, 9, 3, 7, 6, 10, 5, 7, 11, 9, 4, 8, 11, 2, 7, 12, 5, 9, 13,
     10, 11, 4, 8, 9, 13, 7, 5, 10]
]

free_table = [
    [11, 12, 8, 7, 11, 1, 8, 12, 10, 6, 8, 5, 12, 1, 9, 1, 10, 11, 6, 9, 5, 10, 13, 7, 11, 1, 10, 12, 1, 5, 9, 8, 5, 11,
     6, 7, 1, 1, 1, 10, 7, 13, 8, 9],
    [8, 6, 12, 11, 1, 1, 6, 5, 8, 9, 10, 1, 1, 1, 11, 9, 10, 7, 8, 5, 9, 6, 11, 12, 8, 1, 7, 10, 1, 8, 9, 13, 12, 11, 7,
     9, 5, 7, 6, 1, 8, 9, 13, 7],
    [11, 13, 8, 12, 1, 10, 11, 6, 1, 9, 5, 8, 10, 6, 1, 9, 10, 1, 1, 7, 13, 9, 1, 10, 6, 8, 12, 5, 11, 6, 9, 7, 5, 12,
     1, 11, 10, 12, 7, 11, 8, 9],
    [9, 7, 6, 8, 12, 1, 10, 11, 1, 7, 8, 12, 1, 11, 9, 5, 7, 10, 11, 6, 1, 7, 8, 13, 9, 5, 11, 1, 1, 1, 12, 10, 6, 7,
     13, 8, 6, 11, 10, 1, 9, 12, 1],
    [10, 1, 11, 9, 8, 5, 7, 10, 12, 8, 13, 11, 9, 6, 1, 12, 11, 7, 10, 8, 9, 7, 1, 12, 9, 10, 1, 12, 1, 8, 7, 11, 10, 5,
     9, 13, 7, 12, 6, 1, 5, 8]
]
# Расчет вероятностей для таблицы Main
main_probabilities = calculate_probabilities([symbol for row in main_table for symbol in row])

# Расчет вероятностей для таблицы Free
free_probabilities = calculate_probabilities([symbol for row in free_table for symbol in row])

# Расчет математического ожидания
expected_value = 0

for combination, probability in main_probabilities.items():
    paytable_combination_value = 0
    for symbol, symbol_count in combination.items():
        paytable_combination_value += paytable[symbol][symbol_count]
    expected_value += probability * paytable_combination_value

for combination, probability in free_probabilities.items():
    free_paytable_combination_value = 0
    for symbol, symbol_count in combination.items():
        free_paytable_combination_value += free_paytable[symbol][symbol_count]
    expected_value += probability * free_paytable_combination_value

print("Expected Value:", expected_value)
