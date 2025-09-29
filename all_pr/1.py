'''
def say_hello():
    print("hello")

def say_hello():
    print("hello")
print("bye")

def say_hello():
    print("hello")
say_hello()
say_hello()
say_hello()
say_hello()

def say_hello(): print("hello")

say_hello()

def say_hello():
    print("hello")
def say_goodbye():
    print("good bye")
say_hello()
say_goodbye()

def print_message():
    def say_hello(): print("hello")
    def say_goodbye(): print("good bye")
    say_hello()
    say_goodbye()
print_message()

def main():
    say_hello()
    say_goodbye()
def say_hello():
    print("hello")
def say_goodbye():
    print("good bye")
main()

def say_hello(name):
    print(f"hello, {name}")
say_hello("Natale")

def print_person(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")
print_person("Natale", 25)

def say_hello(name="Tom"):
    print(f"Hello, {name}")
say_hello()
say_hello("Bob")

def print_person(name, age = 18):
    print(f"Name: {name} Age:{age}")
print_person("Bob")
print_person("Tom", 37)

def print_person(name, *, age, company):
    print(f"Name: {name} Age: {age} Company: {company}")
print_person("Bob", age = 21, company = "Microsoft")

def print_person(name, /, age, company="Microsoft"):
    print(f"Name: {name} Age: {age} Company: {company}")
print_person("Tom", company="JetBrains", age=24)
print_person("Bob", 41)

def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")
sum(1, 2, 3, 4, 5)
sum(3, 4, 5, 6)

def get_message():
    return "Hello METANIT.COM"
message = get_message()
print(message)

def double(number):
    return 2 * number
result1 = double(4)
result2 = double(5)
print(f"result1 = {result1}")
print(f"result2 = {result2}")

def sum(a, b):
    return a + b
result = sum(4, 6)
print(f"sum(4, 6) = {result}")
print(f"sum(3, 5) = {sum(3, 5)}")

def print_person(name, age):
    if age > 120 or age < 1:
        print("invalid age")
        return
    print(F"Name: {name} Age: {age}")
print_person("Tom", 22)
print_person("Bob", -120)

def say_hello(): print("Hello")
def say_goodbye(): print("Good Bye")
message = say_hello
message()
message = say_goodbye
message()

def sum(a, b): return a + b
def multiply(a, b): return a * b
operation = sum
result = operation(5, 6)
print(result)
operation = multiply
print(operation(5, 6))

def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply
operation = select_operation(1)
print(operation(10, 6))
operation = select_operation(2)
print(operation(10, 6))
operation = select_operation(3)
print(operation(10, 6))

message = lambda: print("Hello")
message()

square = lambda n: n * n
print(square(4))
print(square(5))

sum = lambda a, b: a + b
print(sum(4, 5))
print(sum(5, 6))

def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
do_operation(5, 4, lambda a, b: a + b)
do_operation(5, 4, lambda a, b: a * b)

def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b
opertion = select_operation(1)
print(opertion(10, 6))
opertion = select_operation(2)
print(opertion(10, 6))
opertion = select_operation(3)
print(opertion(10, 6))
'''