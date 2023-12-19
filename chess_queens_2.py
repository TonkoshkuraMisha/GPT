def write_all_minimal_queen_placements(file_path):
    n = 8  # Размер доски
    board = [[0 for _ in range(n)] for _ in range(n)]

    with open(file_path, 'w') as file:
        for i in range(n):
            current_board = [[0 for _ in range(n)] for _ in range(n)]
            current_board[i][i] = 1  # Расположение ферзя в каждой строке
            for row in current_board:
                file.write(' '.join(map(str, row)) + '\n')
            file.write('\n')

    print(f"All possible combinations for minimal {n}-queens saved to {file_path}")


if __name__ == "__main__":
    file_path = 'minimal_queen_placements.txt'
    write_all_minimal_queen_placements(file_path)
