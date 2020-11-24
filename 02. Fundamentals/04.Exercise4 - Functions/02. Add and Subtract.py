def subtract(summed, c):
    return summed - c


def sum_numbers(a, b):
    return a + b


def add_and_subtract(a, b, c):
    res = sum_numbers(a, b)
    return subtract(res, c)


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
