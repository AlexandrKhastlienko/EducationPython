# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m,
# заполнив её в соответствии с образцом.
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Sample Input 1:
#
# 5 5
# Sample Output 1:
#
# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4


def recurse(n, m):
    matrix = [[max(m, n)] * m for i in range(n)]

    for i in range(n):
        num = (i % m) + 1
        for j in range(m):
            matrix[i][j] = num
            num += 1
            if num > m:
                num = 1

    return "\n".join(" ".join(str(x) for x in row) for row in matrix)


n, m = map(int, input().split())
print(recurse(n, m))
