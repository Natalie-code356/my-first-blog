'''
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
while True:
    selection = int(input("1.Запись в файл\t\t2.Чтение файла\t\t3.Выход\nВыберите действие: "))
    match selection:
        case 1 : write()
        case 2 : read()
        case 3 : break
        case _ : print("Некорректный ввод")
print("Программа завершена")

import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (72,60,50)
RED = (123,0,28)
BLUE = (65,105,255)
running = True
while running:
    for event in pygame.event.get():
        running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, BROWN, (100,200,200,150))
    pygame.draw.polygon(screen, RED,[(100,200), (200,100), (300,200)])
    pygame.draw.rect(screen, BLACK, (180,280,40,70))
    pygame.draw.rect(screen, BLUE, (130,230,50,40))
    pygame.draw.line(screen, BLACK, (155,230), (155,270), 2)
    pygame.draw.line(screen, BLACK, (155,230), (155,270), 2)
    pygame.display.flip()
pygame.quit()
quit()
'''