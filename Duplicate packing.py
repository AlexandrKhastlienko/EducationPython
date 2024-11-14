# На вход программе подается строка текста, содержащая символы.
# Напишите программу, которая упаковывает последовательности одинаковых
# символов заданной строки в подсписки.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести указанный вложенный список.


word = input().replace(" ", "")
dub = []

for i in range(len(word)):

    if dub and word[i] in dub[-1]:
        continue

    sublist = []
    for j in range(i, len(word)):
        if j < len(word) - 1 and word[j] == word[j + 1]:
            sublist.append(word[j])
        else:
            sublist.append(word[j])
            break

    dub.append(sublist)

print(dub)
