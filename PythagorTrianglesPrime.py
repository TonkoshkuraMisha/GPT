def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_pythagorean_triples(count):
    triples = []
    m, n = 2, 1

    while len(triples) < count:
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2

        triple = tuple(sorted([a, b, c]))
        triples.append(triple)

        n += 1
        if n == m:
            n = 1
            m += 1

    return triples


def filter_two_prime_triples(triples):
    return [triple for triple in triples if sum(is_prime(num) for num in triple) >= 2]


def main():
    try:
        count = int(input("Введите количество Пифагоровых троек: "))
        if count <= 0:
            print("Пожалуйста, введите положительное число.")
        else:
            all_triples = generate_pythagorean_triples(count)
            two_prime_triples = filter_two_prime_triples(all_triples)

            if two_prime_triples:
                print(f"{count} Пифагоровых троек с не менее чем двумя простыми числами:")
                for triple in two_prime_triples:
                    print(triple)
            else:
                print("В данных пределах нет Пифагоровых троек с не менее чем двумя простыми числами.")
    except ValueError:
        print("Пожалуйста, введите корректное число.")


if __name__ == "__main__":
    main()
