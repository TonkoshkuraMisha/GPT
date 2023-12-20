from mpmath import mp


def calculate_pi(digits):
    mp.dps = digits + 2  # Устанавливаем точность, добавив два дополнительных знака

    pi_value = mp.pi
    return str(pi_value)[:-1]  # Избавляемся от лишнего 3 в конце


def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content + "\n")


def main():
    digits = int(input("Введите количество знаков после запятой для числа π: "))

    pi_result = calculate_pi(digits)

    # Выводим результаты в консоль
    print(f"Число π с {digits} знаками после запятой: {pi_result}")

    # Создаем имя файла с учетом количества знаков после запятой
    filename = f"pi_results_{digits}_digits.txt"

    # Сохраняем результаты в файл (перезаписываем файл)
    save_to_file(filename, f"Число π с {digits} знаками после запятой: {pi_result}")

    print(f"Результаты сохранены в файл '{filename}'.")


if __name__ == "__main__":
    main()
