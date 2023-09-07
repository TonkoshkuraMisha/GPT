def is_safe(board, row, col, n):
    # Проверка по вертикали вверх
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Проверка по левой диагонали вверх
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Проверка по правой диагонали вверх
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_queens(board, row + 1, n):
                return True
            board[row][col] = 0

    return False


def print_solution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))


n = 8  # Размер шахматной доски
chess_board = [[0] * n for _ in range(n)]

if solve_queens(chess_board, 0, n):
    print_solution(chess_board)
else:
    print("Решение не найдено.")
