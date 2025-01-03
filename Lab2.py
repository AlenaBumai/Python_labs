from random import randint
import random
import numpy
import numpy as np

#Вариант 3
#Найдите сумму отрицательных элементов списка.
#Найдите сумму элементов списка между двумя первыми нулями.
# Если двух нулей нет в списке, то выведите ноль.
print("задание 3. Найдите сумму отрицательных элементов списка. ")

print ("Введите размер массива")
n=int(input())
A=[random.randint(-30, 30) for i in range(n)]
print(A)
s=0
for i in range(n):
   if A[i]<0:
       s=s+A[i]
print (f"сумма отрицательных элементов - {s}")

print(" Найдите сумму элементов списка между двумя первыми нулями. ")
s=0
if A.count(0)==0:
    print(f"{A.count(0)}  - нулей в списке")
elif A.count(0)==1:
    print(f"{A.count(0)}  - ноль в списке")
elif A.count(0) >= 2:
    for i in range(A.index(0)+1,n):
        s = s + A[i]
        if A[i] != 0:
            break

    print(f"{s}  - сумма элементов списка между двумя первыми нулями")

#Вариант 4
#Найдите произведение элементов списка с нечетными номерами.
#Найдите наибольший элемент списка, затем удалите его и выведите новый список.

print("задание 5. Найдите произведение элементов списка с нечетными номерами")

D=[random.randint(1, 100) for i in range(50)]
print(D)
s=1
for i in range (1, (len(D))):
        if i%2!=0:
            s = s*D[i]
print(f"{s}  - произведение элементов списка с нечетными номерами")

print("Найдите наибольший элемент списка, затем удалите его и выведите новый список")
print(f"{max(D)} - наибольший элемент списка")
D.pop(D.index(max(D)))
print("список без наибольшего элемента")
print(D)


#Задание 2. Задачи на многомерные списки
#Выберете одну из задач:
#1.	В матрице найти номер строки, сумма чисел в которой максимальна.

print("Задание 2. Задачи на многомерные списки")
print("В матрице найти номер строки, сумма чисел в которой максимальна")
np_arr1 = np.array(
[[random.randint(0, 10), random.randint(1, 10), random.randint(1, 10)],
[random.randint(0, 10), random.randint(1, 10), random.randint(1, 10)],
[random.randint(0, 10), random.randint(1, 10), random.randint(1, 10)],
[random.randint(0, 10), random.randint(1, 10), random.randint(1, 10)]])

print(np_arr1)
MaxS=0
MaxI=0

for i in range(len(np_arr1)):
    S = 0
    for j in range(3):
        S=S+np_arr1[i][j]
    if S>MaxS:
        MaxS=S
        MaxI=i
print(f"{MaxS} - наибольшая сумма строки, {MaxI} - номер такой строки")



