import sys

sys.setrecursionlimit(5000)


def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


print(fact(1000))
