# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
# Север и Юг


def max_one(n):
    arr = [[int(_) for _ in input().split()] for _ in range(n)]
    max_num = []

    for i in range(n):
        for j in range(n):
            if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
                max_num.append(arr[i][j])

    return max(max_num)


n = int(input())

print(max_one(n))
