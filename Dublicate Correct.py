# На вход программе подается строка, содержащая строки-идентификаторы.
# Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов.
# Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз,
# сколько такой идентификатор уже встречался.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.

# Sample Input 1:
#
# a b c a a d c
# Sample Output 1:
#
# a b c a_1 a_2 d c_1


words_list = input().split()

dublicate = {}
cor_dub = []
for dub in words_list:
    if dub not in cor_dub:
        cor_dub += [dub]
    else:
        dublicate[dub] = dublicate.get(dub, 0) + 1
        word = dub + "_" + str(dublicate[dub])
        cor_dub.append(word)

print(*cor_dub)