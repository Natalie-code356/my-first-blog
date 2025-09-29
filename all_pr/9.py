'''
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
cat1 = Cat("Барсик", 2)
cat2 = Cat("Муся", 5)
print(cat1.name, cat1.age)
print(cat2.name, cat2.age)

import message
print(message.hello)
message.print_message("Hello work")
import message as mes
print(mes.hello)
mes.print_message("Hello work")

FILENAME = "message.txt"
def write():
    message = input("Введите строчку: ")
    with open(FILENAME, "a") as file:
        file.write(message + "\n")
def read():
    with open(FILENAME, "r") as file:
        for message in file:
            print(message, end=" ")
    print()
while(True):
    selection = int(input("1.Запись в файл\t\t2.Чтение файла\t\t3.Выход\nВыберите действие: "))
    match selection:
        case 1 : write()
        case 2 : read()
        case 3 : break
        case _ : print("Некорректный ввод")
print("Программа завершена")

import os


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()
'''