# Напишите функцию get_next_prime(num),
# которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число большее числа num.


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def get_next_prime(x):
    x += 1
    while True:
        find_prime = is_prime(x)
        if find_prime:
            return x
        x += 1


x = int(input())

print(get_next_prime(x))
