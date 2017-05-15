def factorial(n):
    if n <= 1:
        return n
    else:
        return factorial(n - 1) * n


def CountPath(n):
    res = factorial(n * 2) / (factorial(n) * factorial(n))
    return res


if __name__ == '__main__':

    print CountPath(20)
