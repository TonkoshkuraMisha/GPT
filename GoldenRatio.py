from mpmath import mp


def calculate_golden_ratio(digits):
    mp.dps = digits + 2  # Устанавливаем точность, добавив два дополнительных знака
    golden_ratio = (1 + mp.sqrt(5)) / 2
    return str(golden_ratio)[:-1]  # Избавляемся от лишнего 2 в конце


def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content + "\n")


def main():
    digits = int(input("Введите количество знаков после запятой для золотого сечения: "))

    golden_ratio_result = calculate_golden_ratio(digits)

    # Выводим результаты в консоль
    print(f"Золотое сечение с {digits} знаками после запятой: {golden_ratio_result}")

    # Создаем имя файла с учетом количества знаков после запятой
    filename = f"golden_ratio_results_{digits}_digits.txt"

    # Сохраняем результаты в файл (перезаписываем файл)
    save_to_file(filename, f"Золотое сечение с {digits} знаками после запятой: {golden_ratio_result}")

    print(f"Результаты сохранены в файл '{filename}'.")


if __name__ == "__main__":
    main()
