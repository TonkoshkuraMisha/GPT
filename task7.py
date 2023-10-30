import sys
import time

sys.setrecursionlimit(3000)
sys.set_int_max_str_digits(50000)

# точка отсчета времени
start = time.time()

# циклический факториал
# def factorial(x):
#     a = 1
#     for i in range(2, x + 1):
#         a = a * i
#     return a


# рекурсивный факториал
def factorial(x):
    if x == 0:
        return 1
    return factorial(x - 1) * x


print(factorial(2995))

# собственно время работы программы
end = time.time() - start

# вывод времени
print(end)