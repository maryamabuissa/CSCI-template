import pygame, itertools

def fade_into(c1, c2, n):
    """ Give the next color to draw \n"""
    "Args: c1,c2 => colors, n => int"
    dif = [(c1[i]-c2[i])/float(n) for i in range(3)] # calculate the per-frame difference
    return [c1[i]-dif[i] for i in range(3)] # subtract that difference

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

FADE_SPEED = 80 # no of frames for shifting

colors = (RED, BLACK, BLUE) # to allow you to iterate over the colors

SIZE = (1000,1000)
screen = pygame.display.set_mode(SIZE)

# to cycle through the colors
cycle = itertools.cycle(colors)

## needed for fading
c_color = next(cycle) # RED    current_color
n_color = next(cycle) # BLACK  next_color
frames = FADE_SPEED        
## --------------

clock = pygame.time.Clock() # regulate fps

pos = 0

while True:
    # handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close window event
            pygame.quit()

    c_color = fade_into(c_color, n_color, frames) # get next color
    pos += 1
    if pos == SIZE[0]:
        break

    screen.fill(BLACK)
    pygame.draw.circle(screen,tuple(map(int,c_color)),(pos, pos),200)
    pygame.display.flip()

    frames -= 1
    if frames == 0: # translation complete
        frames = FADE_SPEED
        n_color = next(cycle) # get next color

    clock.tick(40) # run at maximum of 40 frames per second
