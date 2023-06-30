def fib():
    first = 0
    last = 1
    while True:
        first, last = last, first + last
        yield first


f = fib()
for i in range(1, 1001):
    print(f'fib{i} = {next(f)}')
