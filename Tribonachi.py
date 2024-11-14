# Напишите программу, которая считывает натуральное число n
# и выводит первые n чисел последовательности Трибоначчи.

fib1 = fib2 = fib3 = 1

n = int(input())

if n < 3:
    print("1 " * n, end=" ")
else:
    print(fib1, fib2, fib3, end=" ")


for i in range(3, n):
    fib1, fib2, fib3 = fib2, fib3, fib1 + fib2 + fib3
    print(fib3, end=" ")
