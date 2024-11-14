# На вход программе подаются два предложения. Напишите программу, которая определяет,
# являются они анаграммами или нет. Ваша программа должна игнорировать регистр символов,
# знаки препинания и пробелы.
#
# Формат входных данных
# На вход программе подаются два предложения, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.


def count_alpha(word):
    dic = {}
    for ch in word.lower():
        if ch.isalpha():
            dic[ch] = dic.get(ch, 0) + 1

    return dic


print("YES" if count_alpha(input()) == count_alpha(input()) else "NO")