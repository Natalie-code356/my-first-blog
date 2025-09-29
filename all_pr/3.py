'''
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print("Первое число больше чем второе")
elif a == b:
    print("Числа равны")
else:
    print("Второе число больше чем первое")

a = input("Введите ваше имя: ")
b = input("введите вашу фамилию: ")
print(f"Вас зовут, {a}, {b}")

for a in range(20):
   a = input("Введите фамилию: ")

for n in range(7, 22):
    print(n, end=" ")

age = 22
message = "Age: " + str(age)
print(message)

name = "Tom"
def say_hi():
    print("Hello", name)
def say_bey():
    print("Good bye", name)
say_hi()
say_bey()

def say_hi():
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)
def say_bye():
    name = "Tom"
    print("Good bye", name)
say_hi()
say_bye()

for n in range(0, 52, 2):
    print(n, end=" ")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
for a in range(a, b):
    if a % 2==0:
        print(a, end=" ")

a = int(input("Введите ваше число: "))
if a % 2==0:
    print("Число чётное")
else:
    print("Число не чётное")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a > b > c:
    print("Первое число большее")
elif a > b < c:
    print("Первое число большее")
elif a > b == c:
    print("Первое число большее")
elif a < b > c:
    print("Второе число большее")
else:
    print("Третье число большее")
'''