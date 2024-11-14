# На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки
# в один отсортированный список с помощью функции quick_merge(), а затем выводит его.
# писки чисел. Напишите программу, которая объединяет указанные списки в один отсортированный
# список с помощью функции quick_merge(), а затем выводит его.


def quick_merge(list1, list2):
    result = []

    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    else:
        result += list2[p2:]

    return result


n = int(input())

list1 = [int(dig) for dig in input().split()]

for num in range(n - 1):
    list2 = [int(x) for x in input().split()]
    list1 = quick_merge(list1, list2)

print(*list1)
