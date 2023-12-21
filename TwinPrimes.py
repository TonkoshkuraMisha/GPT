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


def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content + "\n")


def main():
    try:
        n = int(input("Введите количество простых чисел-близнецов: "))
        if n <= 0:
            raise ValueError("Число должно быть положительным.")

        twin_primes = generate_twin_primes(n)

        print(f"{n} первых простых чисел-близнецов:")
        for twin_prime in twin_primes:
            print(twin_prime)

        filename = f"twin_primes_{n}.txt"
        content = f"{n} первых простых чисел-близнецов:\n{twin_primes}"

        save_to_file(filename, content)
        print(f"Информация сохранена в файл '{filename}'.")

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
