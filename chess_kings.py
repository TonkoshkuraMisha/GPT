def count_king_arrangements(board_size):
    if board_size < 2:
        return 0

    total_arrangements = 0
    for row1 in range(board_size):
        for col1 in range(board_size):
            for row2 in range(board_size):
                for col2 in range(board_size):
                    if abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1:
                        continue  # Kings are attacking each other
                    total_arrangements += 1

    return total_arrangements


board_size = 8  # Размер шахматной доски
arrangements = count_king_arrangements(board_size)
print(f"Количество возможных расстановок двух королей на доске {board_size}x{board_size}: {arrangements}")
