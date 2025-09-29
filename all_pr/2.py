'''
name = input("введите ваше имя: ")
print("Привет", name)
age = input(f"{name}, сколько тебе лет?")
print("тебе ", age, " лет")

a = input("введите первое число: ")
b = input("введите второе число: ")
print(f"операция с числами: ")
print(f"сложение {int(a) + int(b)}")
print(f"вычитание {int(a) - int(b)}")
print(f"умножение {int(a) * int(b)}")
print(f"деление {int(a) / int(b)}")

p = float(input("Начальная сумма вклада: "))
r = float(input("Процент по вкладу: "))
t = float(input("Количество лет: "))
si = (p * r * t) / 100
print("Начисленные проценты: ", si)

message = lambda: (print("Hello"))
message()

square = lambda n: n * n
print(square(4))
print(square(5))

sum = lambda a, b: a + b
print(sum(4, 6))
print(sum(8, 8))

def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
do_operation(5, 4, lambda a, b: a + b)
do_operation(5, 4, lambda a, b: a * b)

def select_operatio(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b
operation = select_operatio(1)
print(operation(10, 6))
operation = select_operatio(2)
print(operation(10, 6))
operation = select_operatio(3)
print(operation(10, 6))

a = 2
b = 2.5
c = a + b
print(c)

a = int(15)
b = int(3.7)
c = int("4")
e = int(False)
f = int(True)
print(a)
print(b)
print(c)
print(e)
print(f)

a = "2.7"
b = 3
c = float(a) + b
print(c)

a = float(15)
b = float(3.7)
c = float("4.7")
d = float("5")
e = float(False)
f = float(True)
print(a)
print(b)
print(c)
print(e)
print(f)

a = str(False)
b = str(True)
c = str(5)
d = str(5.7)
print(a)
print(b)
print(c)
print(d)
'''