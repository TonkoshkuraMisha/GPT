def generate_pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


def print_colored_pascal_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        row_str = " ".join(map(str, row))
        padding = (max_width - len(row_str)) // 2
        print(" " * padding, end="")

        for num in row:
            print(f"\033[32m{num}\033[0m", end=" ")  # Зелёный цвет

        print()


def main():
    try:
        rows = int(input("Введите количество строк для треугольника Паскаля: "))
        if rows < 0:
            print("Пожалуйста, введите неотрицательное число.")
        else:
            pascal_triangle = generate_pascal_triangle(rows)
            print_colored_pascal_triangle(pascal_triangle)
    except ValueError:
        print("Пожалуйста, введите корректное число.")


if __name__ == "__main__":
    main()
