# На вход программе подается натуральное число
# и строк, а затем число
# Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
words = []

for i in range(n):
    words.append(input())

k = int(input()) - 1

for ch in words:
    if len(ch) > k:
        print(ch[k], end="")
