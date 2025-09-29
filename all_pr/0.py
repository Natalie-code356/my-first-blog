'''
language = "english"
if language == "english":
    print("hello")
print("end")

language = "russian"
if language == "english":
    print("hello")
else:
    print("привет")
print("end")

language = "russian"
if language == "english":
    print("hello")
    print("world")
else:
    print("привет")
    print("мир")

language = "german"
if language == "english":
    print("hello")
    print("world")
elif language == "german":
    print("hallo")
    print("welt")
else:
    print("привет")
    print("мир")

language = "german"
if language == "english":
    print("hello")
elif language == "german":
    print("hallo")
elif language == "french":
    print("salut")
else:
    print("привет")

language = "english"
daytime = "morning"
if language == "english":
    print("English")
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")

language = "russian"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")

number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")

number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

number = 10

while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

message = "hello"

for c in message:
    print(c)

for n in range(10):
    print(n, end=" ")

message = "hello"
for c in message:
    print(c)
else:
    print(f"Последний символ: {c}. Цикл завершен");
print("Работа программы завершена")

i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i+= 1

for c1 in "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")

number = 0
while number < 5:
    number += 1
    if number == 3:
        break
    print(f"number = {number}")

number = 0
while number < 5:
    number += 1
    if number == 3:
        continue
    print(f"number = {number}")
'''
