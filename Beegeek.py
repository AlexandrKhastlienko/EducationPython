# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password),
# которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True,
# если пароль является действительным паролем BEEGEEK банка, или False в противном случае.

# разрезать пароль на три части
# первая до первого вхождения двоеточия
# вторая между первым и вторым двоеточием
# третья после второго вхождения двоеточия


def is_valid_password(password):
    if password.count(":") > 2:
        return False

    a_valid = False
    b_valid = False
    c_valid = False

    colon = password.find(":")
    r_colon = password.rfind(":")

    a_cut = password[:colon]
    b_cut = password[colon + 1 : r_colon]
    c_cut = password[r_colon + 1 :]

    dig_b = int(b_cut)
    dig_c = int(c_cut)

    cnt_a = 0
    for i in range(len(a_cut)):
        if a_cut[i] != a_cut[-(i + 1)]:
            cnt_a += 1
    if cnt_a == 0:
        a_valid = True

    cnt_b = 0
    for i in range(1, dig_b + 1):
        if dig_b % i == 0:
            cnt_b += 1
    if cnt_b == 2:
        b_valid = True

    if dig_c % 2 == 0:
        c_valid = True

    return all([a_valid, b_valid, c_valid])


password = input()

print(is_valid_password(password))
