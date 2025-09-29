'''
a = int(input("Введите количество элементов списка: "))
c = []
for a in range(0, a):
  b = int(input(f"Введите {a + 1} число: "))
  c.append(b)
print("Список:",c)
print("Сумма:", sum(c))
t = sum(c)/len(c)
print("Среднее арифметитечское значение:",t)
Min = min(c)
Max = max(c)
print("Минимум:",Min)
print("Максимум:",Max)
v = [n for n in c if n < 0]
if v:
    print("Количество отрицательных чисел:", len(v))
    print("Отрицательные числа:",v)
e = [n for n in c if n % 2 == 0]
if e:
    print("Чётные числа:", e)
'''
