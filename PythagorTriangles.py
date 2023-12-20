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


def main():
    try:
        count = int(input("Введите количество Пифагоровых троек: "))
        if count <= 0:
            print("Пожалуйста, введите положительное число.")
        else:
            triples = generate_pythagorean_triples(count)
            print(f"{count} Пифагоровых троек:")
            for triple in triples:
                print(triple)
    except ValueError:
        print("Пожалуйста, введите корректное число.")


if __name__ == "__main__":
    main()
