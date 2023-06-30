def factorize(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            count = 0
            while n % divisor == 0:
                n = n // divisor
                count += 1
            factors.append((divisor, count))
        divisor += 1

    return factors


# Запитуємо користувача про число
number = int(input("Введіть натуральне число: "))

# Розкладаємо число на прості множники
result = factorize(number)

# Виводимо результат
print("Розклад числа", number, "на прості множники:")
for i, (factor, exponent) in enumerate(result):
    if exponent == 1:
        print(factor, end="")
    else:
        print("(", factor, "^", exponent, ")", end="")

    if i < len(result) - 1:
        print(" * ", end="")
    else:
        print()

