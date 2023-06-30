
def count_cases(s: int, a: int, b: int):
    count = 0
    for i in range(100):
        for j in range(100):
            if i * a - j * b == s:
                count += 1
    return count


print(count_cases(250, 20, 25))
