# На вход программе подается строка текста, содержащая символы. Из данной строки формируется список.
# Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести указанный список, содержащий все возможные подсписки, включая пустой список


def sublist_list(letters):
    result = [[]]
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            result.append(letters[i:j])
    return result


def sorted_key(letters):
    for_sort = sublist_list(letters)

    return sorted(for_sort, key=len)


letters = list(input().split())


print(sorted_key(letters))
