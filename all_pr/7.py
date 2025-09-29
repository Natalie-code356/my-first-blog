'''
a = int(input("Введите количество элементов списка: "))
c = []
for a in range(0, a):
  b = int(input(f"Введите {a + 1} число:"))
  c.append(b)
print("Список:", c)
m = sum(c)
print("Сумма:", m)
e = [n for n in c if n % 2 == 0]
if e:
    print("Чётные числа:", e)
d = [n for n in c if n % 2 != 0]
if d:
    print("Список:", d)

from django.template.defaultfilters import random

a = int(input("Введите число: "))

while a != 0:
    b = sum
    print(f"number = {a}")
else:
    print(f"number = {a}. Работа цикла завершена")
print("Работа программы завершена")
'''