import time
import random
import sys


def generate_array(length, min_value, max_value):
    array = []
    for i in range(length):
        array.append(random.randint(min_value, max_value))
    return array


def quicksort(array, depth=None):
    if depth is None:
        depth = sys.getrecursionlimit()

    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    smaller = [x for x in array if x < pivot]
    larger = [x for x in array if x >= pivot]

    if depth <= 0:
        return array

    return quicksort(smaller, depth - 1) + [pivot] + quicksort(larger, depth - 1)


def measure_sort_time(length, min_value, max_value, depth):
    array = generate_array(length, min_value, max_value)

    start = time.time()
    quicksort(array, depth)
    end = time.time()

    return end - start


if __name__ == "__main__":
    length = 10
    min_value = -50
    max_value = 50
    depth = 10000000

    sort_time = measure_sort_time(length, min_value, max_value, depth)

    print(f"Время сортировки массива размером {length}: {sort_time:.2f} секунд")
