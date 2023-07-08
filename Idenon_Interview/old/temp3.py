def calculate_symbol_probabilities(spins):
    symbol_counts = {symbol_id: 0 for symbol_id in range(1, 14)}  # Счетчики вхождений символов

    total_spins = len(spins)
    for spin in spins:
        for symbol_id in spin:
            symbol_counts[symbol_id] += 1

    symbol_probabilities = {symbol_id: count / total_spins for symbol_id, count in symbol_counts.items()}
    return symbol_probabilities


# Расчет вероятностей выпадения символов для основных спинов и фригейма
main_spins_probabilities = calculate_symbol_probabilities(main_spins)
free_spins_probabilities = calculate_symbol_probabilities(free_spins)
