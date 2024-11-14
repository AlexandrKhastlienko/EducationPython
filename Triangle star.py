# Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник
# с основанием и высотой равными 15 и 8 соответственно:


def draw_triangle(elem):
    for i in range(8):
        now_draw = (" " * (7 - i)) + (elem + elem * 2 * i)
        print(now_draw)


draw_triangle("*")
