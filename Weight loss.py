# Гвидо, засевший за компьютером и не ведущий активный образ жизни, «немного» поднабрал в весе.
# Осталось всего 60 дней до лета, а хочется быть в форме.
# Вот Гвидо и решился на похудение. Все дни до лета он пронумеровал
# от 1 до 60 (включительно).
# Перед началом похудения у Гвидо был вес
# 100 кг, а своей целью он поставил достичь веса
# 88 кг (или меньше). Он решил худеть на одну и ту же массу ежедневно.
#
# Напишите программу, которая принимает на вход текущий день и текущий вес Гвидо. Программа должна вывести фразу:
#
# «Все идет по плану» (без кавычек), если Гвидо удаётся держать планку в похудении и его вес ниже либо равен тому,
# который он запланировал на текущий день
# «Что-то пошло не так» (без кавычек), если Гвидо не очень старается и его вес выше того,
# который он запланировал на текущий день
# Также программа должна вывести информацию о номере дня похудения, текущем весе Гвидо и цели по весу на текущий день в формате:
#
# #<номер дня> ДЕНЬ: ТЕКУЩИЙ ВЕС = <текущий вес Гвидо> кг, ЦЕЛЬ по ВЕСУ = <цель по весу на текущий день> кг
# Формат входных данных
# На вход программе подаются два числа (каждое на новой строке): номер дня похудения (целое число) и текущий вес Гвидо (действительное число).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.


day, current_weight = int(input()), float(input())

less = 12 / 60
start_weight = 100

normal_less = start_weight - (day * less)

if normal_less < current_weight:
    print("Что-то пошло не так")
elif normal_less >= current_weight:
    print("Все идет по плану")
print(
    f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {normal_less} кг",
)
