# Напишите функцию compute_binom(n, k),
# которая принимает в качестве аргументов два натуральных числа n и k
# и возвращает значение биномиального коэффициента, равного n!k!/(n−k)!

from math import factorial as f


def compute_binom(n, k):
    return int(f(n) / (f(k) * (f(n - k))))


n, k = map(int, [input(), input()])

print(compute_binom(n, k))
