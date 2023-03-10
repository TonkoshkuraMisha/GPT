import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


number_list = [137, 10e10, 137e10, 137e137]
for i in number_list:
    print(f"{i} is prime number: {is_prime(i)}")
