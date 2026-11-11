import pygame
import random

COLOR = (255, 100, 98)        
SURFACE_COLOR = (0, 155, 50) 
WIDTH = 500
HEIGHT = 500

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()


pygame.init()

RED = (155, 0, 0)  
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("That old TV game if it was Christmas")


all_sprites_list = pygame.sprite.Group()

object_ = Sprite(RED, 20, 30)
object_.rect.x = 200  
object_.rect.y = 300  

all_sprites_list.add(object_)


exit_game = True
clock = pygame.time.Clock()

x_change = 2
y_change = -3
while exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False
    r = object_.rect
    r.x += x_change
    r.y -= y_change
    if r.x > WIDTH or r.x < 0:
        x_change = -x_change
    if r.y > HEIGHT or r.y < 0:
        y_change = -y_change


    all_sprites_list.update()  
    screen.fill(SURFACE_COLOR)  
    all_sprites_list.draw(screen) 
    pygame.display.flip()       
    clock.tick(60)              

pygame.quit()
