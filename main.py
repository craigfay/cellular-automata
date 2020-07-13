import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode([640,600])

red = (230,50,50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    window.fill((40,50,180))
    pygame.draw.rect(window, (200,10,90), Rect((40,40), (90,30)))
    pygame.draw.rect(window, (100,200,250), Rect((320,300), (40,40)))

    pygame.display.update()
