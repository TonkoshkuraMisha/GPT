def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_twin_primes(n):
    twin_primes = []
    current_number = 3

    while len(twin_primes) < n:
        if is_prime(current_number) and is_prime(current_number + 2):
            twin_primes.append((current_number, current_number + 2))
        current_number += 2

    return twin_primes


def generate_twin_prime_differences(twin_primes):
    differences = [twin_primes[i + 1][1] - twin_primes[i][1] for i in range(len(twin_primes) - 1)]
    return differences


def count_elements(differences):
    element_count = {}
    for element in differences:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count


def save_to_file(filename, content):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + "\n")


def main():
    try:
        for power in range(1, 7):  # От 10^1 до 10^6
            n = 10 ** power
            twin_primes = generate_twin_primes(n)
            differences = generate_twin_prime_differences(twin_primes)
            element_count = count_elements(differences)

            filename = f"twin_primes_{n}.txt"
            content = f"{n} первых простых чисел-близнецов:\n{twin_primes}\nРазницы между последними элементами пар:\n{differences}\n\nКоличество каждого элемента в списке differences:\n{element_count}\n\n"

            save_to_file(filename, content)
            print(f"Информация для {n} пар сохранена в файл '{filename}'.")

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
