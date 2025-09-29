'''
import pygame

pygame.init()
screen = pygame.display.set_mode((610, 610))
color = (173, 223, 173)
font = pygame.font.SysFont(None, 25)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    for x in range(10, 600, 50):
        for y in range(10, 600, 50):
            pygame.draw.rect(screen, color, (x, y, 40, 40), 1)
            text_surfase = font.render("y", True, color)
            screen.blit(text_surfase, (x, y))
    pygame.display.update()
quit()
'''