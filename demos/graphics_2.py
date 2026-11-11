import pygame, itertools

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

colors = (RED, BLACK, BLUE) # to allow you to iterate over the colors

SIZE = (1000,1000)
screen = pygame.display.set_mode(SIZE)

# to cycle through the colors
cycle = itertools.cycle(colors) # create an infinite series..

clock = pygame.time.Clock() # regulate fps

while True:
    # handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close window event
            pygame.quit()

    c = next(cycle)
    pygame.draw.circle(screen,c,(500,500),200)
    pygame.display.flip()

    clock.tick(6) # run at maximum 6 frames per second
