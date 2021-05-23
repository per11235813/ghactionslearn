def add(x, y):
    return x + y


def div(x, y):
    return x / y


def fib(n):
    x, y = 0, 1

    for _ in range(n):
        x, y = y, x + y

        yield y
