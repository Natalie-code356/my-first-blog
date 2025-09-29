'''
text = input("Введите предложение: ")
count = len(text)
print("Количество символов:",count)
spaces = text.count(" ")
print("Количество пробелов:",spaces)
new_text = text.replace(" ", "_")
print("предложение с заменёнными пробелами:",new_text)

text = input("Введите слово или предложение: ")
while len(text)> 0:
    print(text)
    text = text[:-1]

text = input("Введите слово или предложение: ")
for i in range(1, len(text) + 1):
    print(text[:i])

numbers = [4, 8, 15, 16, 23, 42]
average = sum(numbers)/len(numbers)
print("среднее арифметитечское значение:", average)
'''