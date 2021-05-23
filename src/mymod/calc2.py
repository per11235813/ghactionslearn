def fac(n):
    if n < 0:
        raise ValueError()

    res = 1
    for i in range(1, n + 1):
        res *= i

    return res
