'''
a = "free68"
b = input("Введите пароль: ")
if a == b:
    print("Пароль верный!")
else:
    print("Пароль неверный!")

num = int(input("Введите число: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

print("Загадай число от 1 до 100, а я попробую его угадать!")

low = 1
high = 100
attempts = 0

while low <= high:
    guess = (low + high) // 2
    attempts += 1
    print(f"Это число {guess}?")
    answer = input("Ответь: да / больше / меньше: ").strip().lower()

    if answer == "да":
        print(f"Ура! Я угадал число {guess} за {attempts} попыток 🎉")
        break
    elif answer == "больше":
        low = guess + 1
    elif answer == "меньше":
        high = guess - 1
    else:
        print("Пожалуйста, пиши только: да / больше / меньше.")

word = input("Введите слово: ")
char = input("Введите символ, который нужно посчитать: ")

count = 0
for letter in word:
    if letter == char:
        count += 1
print(f"Символ '{char}' встречается в слове '{word}' {count} раз(а).")

def outer():
    n = 5
    def inner():
        nonlocal n
        n += 1
        print(n)
    return inner
fn = outer()
fn()
fn()
fn()

def multiply(n):
    def inner(m): return n * m
    return inner
fn = multiply(5)
print(fn(5))
print(fn(6))
print(fn(7))

def multiply(n): return lambda m: n * m
fn = multiply(5)
print(fn(5))
print(fn(6))
print(fn(7))

word = input("Введите слово: ")
if word == word[::-1]:
    print(f"Слово {word} явдяется полидромом")
else:
    print(f"Слово {word} не является полидромом")

def select(input_func):
    def output_func():
        print("*****************")
        input_func()
        print("*****************")
    return output_func
@select
def hello():
    print("Hello METANIT.COM")
hello()
'''
