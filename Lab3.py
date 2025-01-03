
import random
import numpy

# 1 ПУЗЫРЬКОВАЯ СОРТИРОВКА

num = [random.randint(1, 100) for i in range(100)]
for i in range(len(num) - 1):
    for j in range(len(num) - 1 - i):
        if num[j] > num[j + 1]:
            a = num[j + 1]
            num[j + 1] = num[j]
            num[j] = a
print(num)

# 2 ФУНКЦИЯ СОРТИРОВКИ ВСТАВКАМИ insert

num = [random.randint(1, 100) for i in range(100)]
print(num)


def sort_insert(arr):
    n = len(arr)
    for i in range(1, n):
        t = arr[i]
        j = i
        while j != 0:
            if arr[j - 1] > t:
                arr[j] = arr[j - 1]
                j -= 1
            else:
                break
            arr[j] = t


print("сортировка")
sort_insert(num)

# 3 ШЕЙКЕРНАЯ (по псевдокоду, значение массива на позиции 0 не сортирует, остальное сортирует)

num = [random.randint(1, 100) for i in range(100)]
print(num)


def shaker(arr):
    n = len(arr)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            if arr[j] > arr[j + 1]:
                a = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = a

        for g in range(n - 2 - i, i + 1, -1):
            if arr[g] < arr[g - 1]:
                a = arr[g]
                arr[g] = arr[g - 1]
                arr[g - 1] = a

    return arr


print("сортировка")
shaker(num)
print(num)

# 4 ВЫБОРОМ СОРТИРОВКА SELECT

num = [random.randint(1, 100) for i in range(100)]
print(num)


def sort_select(arr):
    n = len(arr)
    for i in range(n - 1):
        m = i
        for j in range(i, n):
            if arr[j] < arr[m]:
                m = j
        a = arr[i]
        arr[i] = arr[m]
        arr[m] = a


print("сортировка")
sort_select(num)

print(num)

# 5 РЕКУРСИЯ, КОЛИЧЕСТВО КВАДРАТОВ В ПРЯМОУГОЛЬНИКЕ

counter = []


def square(num):
    if num[0] != num[1]:
        print(f"{min(num)}  - сторона квадрата {len(counter) + 1}")
        num[num.index(max(num))] = max(num) - min(num)
        counter.append(1)
        return square(num)


print("введите меньшую сторону прямоугольника")
a = int(input())
print("введите большую сторону прямоугольника")
b = int(input())
arr = [a, b]
i = 1
if a == b:
    print("это квадрат")
elif a == 1:
    print(f"одна из сторон равна 1, в прямоугольнике можно разместить  {b} квадратов")
elif b == 1:
    print(f"одна из сторон равна 1, в прямоугольнике можно разместить  {a} квадратов")
else:
    print(square(arr))
    print(f"{len(counter) + 1} - количество квадратов в прямоугольнике")

