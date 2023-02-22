# def count_cases(s: int, a: int, b: int):
#     count = 0
#     a_values = [a * i for i in range(s)]
#     count = sum((s - i_a) % b == 0 for i_a in a_values if s - i_a >= 0)
#     return count
#
#
# print(count_cases(1000, 20, 50))


def count_cases(s: int, a: int, b: int):
    count = 0
    for i in range(100):
        for j in range(100):
            if i * a - j * b == s:
                count += 1
    return count


print(count_cases(250, 20, 25))
