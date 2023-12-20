from mpmath import mp


def calculate_euler_constant(digits):
    mp.dps = digits + 2  # Устанавливаем точность, добавив два дополнительных знака

    euler_constant = mp.euler
    return str(euler_constant)[:-1]  # Избавляемся от лишнего 2 в конце


def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content + "\n")


def main():
    digits = int(input("Введите количество знаков после запятой для постоянной Эйлера: "))

    euler_result = calculate_euler_constant(digits)

    # Выводим результаты в консоль
    print(f"Постоянная Эйлера с {digits} знаками после запятой: {euler_result}")

    # Создаем имя файла с учетом количества знаков после запятой
    filename = f"euler_results_{digits}_digits.txt"

    # Сохраняем результаты в файл (перезаписываем файл)
    save_to_file(filename, f"Постоянная Эйлера с {digits} знаками после запятой: {euler_result}")

    print(f"Результаты сохранены в файл '{filename}'.")


if __name__ == "__main__":
    main()
