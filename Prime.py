# Напишите функцию is_prime(num),
# которая принимает в качестве аргумента натуральное число и возвращает значение True,
# если число является простым, или False в противном случае.


def is_prime(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False


x = int(input())

print(is_prime(x))
