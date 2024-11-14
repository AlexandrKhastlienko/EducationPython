# Магическим квадратом порядка n называется квадратная таблица размер n×n, составленная из всех чисел 1,2,3,…,n**2
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
# Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы:
# n строк, по n чисел в каждой, разделённые пробелами.
# Формат выходных данных
# Программа должна вывести YES, если матрица является магическим квадратом, или NO в противном случае.


def create_matrix(n):
    matrix = [[int(cols) for cols in input().split()] for rows in range(n)]

    main, not_main = [], []
    cols = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            cols[i][j] = matrix[n - j - 1][i]

            if j == 0:
                main.append(matrix[i][i])
                not_main.append(matrix[i][n - i - 1])

    all_nums = [i + 1 for i in range(n**2)]

    sublist = []
    for n in matrix:
        sublist.extend(n)

    return main, not_main, cols, matrix, all_nums, sublist


def check_same(n):
    main, not_main, cols, matrix, all_nums, sublist = create_matrix(n)

    check = [
        sum(main),
        sum(not_main),
    ]

    for i in range(n):
        sum_i_cols = sum(cols[i])
        sum_i_matrix = sum(matrix[i])

        check.append(sum_i_cols)
        check.append(sum_i_matrix)

    check_set = set(check)
    check_digit = set(sublist)
    set_all_nums = set(all_nums)

    if len(check_set) == 1 and check_digit == set_all_nums:
        return "YES"
    else:
        return "NO"


n = int(input())

print(check_same(n))
