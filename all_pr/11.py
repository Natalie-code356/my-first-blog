'''
import math
import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (72,60,50)
RED = (123,0,28)
BLUE = (65,105,255)
ORANGE = (255,153,0)
font = pygame.font.SysFont(None, 30)
t = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.circle(screen, WHITE, (200,300), 60)
    pygame.draw.circle(screen, WHITE, (200,195), 45)
    pygame.draw.circle(screen, WHITE, (200,120), 30)
    pygame.draw.circle(screen, BLACK, (200,300), 60, 2)
    pygame.draw.circle(screen, BLACK, (200,195), 45, 2)
    pygame.draw.circle(screen, BLACK, (200,120), 30, 2)
    pygame.draw.circle(screen, BLACK, (190,115), 4)
    pygame.draw.circle(screen, BLACK, (210,115), 4)
    pygame.draw.polygon(screen, ORANGE, [(200,120), (230,125), (200,130)])
    pygame.draw.circle(screen, BLACK, (200,185), 4)
    pygame.draw.circle(screen, BLACK, (200,205), 4)
    pygame.draw.circle(screen, BLACK, (200,225), 4)
    pygame.draw.rect(screen, BLUE, (170,70,60,20))
    pygame.draw.rect(screen, BLUE, (160,90,80,10))
    offset = int(math.sin(t/10000)*250)
    text_surfase = font.render("Hello",True, BLACK)
    screen.blit(text_surfase, (270,135 + offset))
    pygame.display.flip()
    t += 1
pygame.quit()
quit()
'''