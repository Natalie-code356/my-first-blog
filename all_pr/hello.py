'''
name = input ("Введите ваше имя: ")
print("привет,", name)
print(25+7)
print("hello")
if 5>2:
   print("hello")
print("hello world")
print("full name:", "Natale", "Vasileva")
name = "Biba"
userName =  "Boba"
user_name = "Labubu"
from operator import truediv

isMarried = False
print(isMarried)

isAlive = True
print(isAlive)

age = 21
print("Возраст:", age)

count = 15
print("Количество:", count)

a = 0b11
b = 0b1011
c = 0b100001
print(a)
print(b)
print(c)

a = 0o7
b = 0o11
c = 0o17
print(a)
print(b)
print(c)

a = 0x0A
b = 0xFF
c = 0xA1
print(a)
print(b)
print(c)

height = 1.68
pi = 3.14
weight = 68.
print(height)
print(pi)
print(weight)

x = 3.9e3
print(x)

x = 3.9e-3
print(x)

complexNumber = 1+2j
print(complexNumber)

message = "hello world!"
print(message)
name = 'Tom'
print(name)

text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)

text = Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula
print(text)

text = "Message:\n\"hello world\""
print(text)

path = r"C:python name.txt"
print(path)

userName = "Aboba"
userAge = 56
user = f"name: {userName} age: {userAge}"
print(user)

userId = "abc"
print(userId)

userId = 234
print(userId)

userId = "abc"
print(type(userId))

userId = 234
print(type(userId))

print("hello world", end=" and ")
print("hello METANIT.COM", end=" and ")
print("hello python")

name = input("введите своё имя: ")
print(f"Ваше имя: {name}")

name = input("Your name: ")
age = input("Your age: ")
print(f"Name: {name} Age: {age}")

print(7//2) отбрасывает дробную часть

print(6 ** 2) возводит в степень

print(7%2)

number = 3+4*5**2+7
print(number)

number = (3+4)*(5**2+7)
print(number)

number = 10
number += 5
print(number)

number = 10
number += 5
number -= 3
print(number)

number = 10
number += 5
number -= 3
number *= 4
print(number)

first_number=2.0001
second_number = 5
third_number = first_number / second_number
print(third_number)

first_number=2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number))

first_number=2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number, 4))

print(round(2.49))
print(round(2.51))

print(round(2.5))
print(round(3.5))

print(round(2.554, 2))
print(round(2.5551, 2))
print(round(2.554999, 2))
print(round(2.499, 2))

print(round(2.655, 2))
print(round(2.665, 2))
print(round(2.675, 2))

a = 5
b = 6
result= 5 == 6
print(result)
print(a!=b)
print(a>b)
print(a<b)

bool1 = True
bool2 = False
print(bool1==bool2)

age = 22
weight = 58
result = age > 21 and weight == 58
print(result)

result = 4 and "w"
print(result)

result = 0 and "w"
print(result)

age = 22
isMarried = False
result = age > 21 or isMarried
print(result)

result = 4 or "w"
print(result)

result = 0 or "w"
print(result)

age = 22
isMarried = False
print(not age > 21)
print(not isMarried)
print(not 4)
print(not 0)

message = "hello world"
hello = "hello"
print(hello in message)

gold = "gold"
print(gold in message)

message = "hello world"
hello = "hello"
print(hello not in message)

gold = "gold"
print(gold not in message)
'''