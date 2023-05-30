import pygame

import gameplay_variables
import graphic_engine
import gameplay


pygame.init()
pygame.display.set_caption('Chess opening trainer')

graphic_engine.draw()

while gameplay_variables.run:
    graphic_engine.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameplay_variables.run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            gameplay.mouse_click(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

pygame.quit()
