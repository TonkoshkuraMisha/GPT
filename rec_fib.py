def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])
    return fib[n]


n = 55  # Замените 10 на желаемое число Фибоначчи
result = fibonacci(n)
print(f"F({n}) = {result}")
