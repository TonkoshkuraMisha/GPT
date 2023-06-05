def factorize(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1

    return factors


# Запитуємо користувача про число10
number = int(input("Введіть натуральне число: "))

# Розкладаємо число на прості множники
result = factorize(number)

# Виводимо результат
print("Прості множники числа", number, ":", result)
