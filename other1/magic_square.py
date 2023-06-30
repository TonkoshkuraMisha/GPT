n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# считаем сумму элементов в первой строке и используем ее для проверки магического квадрата
magic_sum = sum(matrix[0])

# проверяем суммы элементов в каждой строке
for i in range(n):
    row_sum = sum(matrix[i])
    if row_sum != magic_sum:
        print("NO")
        exit()

# проверяем суммы элементов в каждом столбце
for j in range(n):
    col_sum = sum(matrix[i][j] for i in range(n))
    if col_sum != magic_sum:
        print("NO")
        exit()

# проверяем сумму элементов по главной диагонали
diag_sum = sum(matrix[i][i] for i in range(n))
if diag_sum != magic_sum:
    print("NO")
    exit()

# проверяем сумму элементов по побочной диагонали
rev_diag_sum = sum(matrix[i][n - 1 - i] for i in range(n))
if rev_diag_sum != magic_sum:
    print("NO")
    exit()

# если все проверки прошли успешно, то матрица является магическим квадратом
print("YES")
