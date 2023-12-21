from mpmath import mp


def calculate_square_root(number, digits):
    mp.dps = digits + 2  # Устанавливаем точность, добавив два дополнительных знака
    square_root_result = mp.sqrt(number)
    return str(square_root_result)[:-1]  # Избавляемся от лишнего 0 в конце


def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content + "\n")


def main():
    number = float(input("Введите число для извлечения квадратного корня: "))
    digits = int(input("Введите количество знаков после запятой: "))

    square_root_result = calculate_square_root(number, digits)

    # Выводим результаты в консоль
    print(f"Квадратный корень из {number} с {digits} знаками после запятой: {square_root_result}")

    # Создаем имя файла с учетом количества знаков после запятой
    filename = f"square_root_results_{number}_{digits}_digits.txt"

    # Сохраняем результаты в файл (перезаписываем файл)
    save_to_file(filename, f"Квадратный корень из {number} с {digits} знаками после запятой: {square_root_result}")

    print(f"Результаты сохранены в файл '{filename}'.")


if __name__ == "__main__":
    main()
