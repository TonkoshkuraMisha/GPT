from mpmath import mp


def calculate_e(digits):
    mp.dps = digits + 2  # Устанавливаем точность, добавив два дополнительных знака

    e_value = mp.e
    return str(e_value)[:-1]  # Избавляемся от лишнего 2 в конце


def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content + "\n")


def main():
    digits = int(input("Введите количество знаков после запятой для числа e: "))

    e_result = calculate_e(digits)

    # Выводим результаты в консоль
    print(f"Число e с {digits} знаками после запятой: {e_result}")

    # Создаем имя файла с учетом количества знаков после запятой
    filename = f"e_results_{digits}_digits.txt"

    # Сохраняем результаты в файл (перезаписываем файл)
    save_to_file(filename, f"Число e с {digits} знаками после запятой: {e_result}")

    print(f"Результаты сохранены в файл '{filename}'.")


if __name__ == "__main__":
    main()
