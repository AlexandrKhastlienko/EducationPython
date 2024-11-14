# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа
# a, b, c – коэффициенты квадратного уравнения
# ax**2+bx+c=0
# ax**2+bx+c=0 и возвращает его корни в порядке возрастания.

import math


def solve(a, b, c):
    d = b**2 - 4 * a * c

    if d < 0:
        return "Нет корней"
    elif d == 0:
        x3 = -b / (2 * a)
        return x3, x3
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        return min(x1, x2), max(x1, x2)


a, b, c = int(input()), int(input()), int(input())

print(*solve(a, b, c))
