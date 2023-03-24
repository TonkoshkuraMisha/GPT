import random

my_list = [random.randint(-1000, 1000) for i in range(1_000_000)]
print(my_list)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)


sorted_arr = quicksort(my_list)
print(sorted_arr)
