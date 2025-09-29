'''
class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

bird1 = Bird("Калибри", 1)
bird2 = Bird("Аист", 3)

class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return (a //b)
    def deduct(self, a, b):
        return a - b
calc = Calculator()
print(calc.add(4, 6))
print(calc.multiply(6, 8))
print(calc.deduct(20, 5))
print(calc.divide(45, 5))

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 * (self.width + self.length)
rect1 = Rectangle (35, 89)
print(rect1.area())
print(rect1.perimeter())

rect2 = Rectangle(10, 25)
print(rect2.area())
print(rect2.area())

class BankAccount:
    def __init__(self, number, sum):
        self.account_number = number
        self.balance = sum
        print(f"Создан счет. Начальный баланс: {sum} единиц")
    def add(self, sum):
        self.balance = self.balance + sum
        print(f"На счет зачислено: {sum} единиц")
    def withdraw(self, sum):
        if self.balance >= sum:
            self.balance = self.balance - sum
            print(f"Со счета снято: {sum} единиц")
        else:
            print("Недостаточно средств на счете")
acc1 = BankAccount("356786554", 3000)
acc1.add(300)
acc1.withdraw(50)
acc1.withdraw(30)
acc1.withdraw(90)
'''
