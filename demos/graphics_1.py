
import pygame
pygame.init()

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
SIZE = (1000,1000)
screen = pygame.display.set_mode(SIZE)
colors = (RED, BLACK, BLUE) # tho allow you to iterate over the colors

for c in colors:
    pygame.draw.circle(screen,c,(500,500),200)
    pygame.display.flip()
    pygame.time.wait(1000)
pygame.quit()
