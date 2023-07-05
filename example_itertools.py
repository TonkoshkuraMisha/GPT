import itertools

s = [1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6]

d = itertools.groupby(s)
for i, j in d:
    print(i, list(j))
