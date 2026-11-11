import pygame


pygame.init()

# create display surface
screen = pygame.display.set_mode((600, 800))

# load image
img = pygame.image.load("/home/mabuissa/Downloads/baby_nu.JPG").convert_alpha()

# resize images
img_large = pygame.transform.scale(img, (600, 800))

running = True
while running:
    # fill background
    screen.fill((255, 255, 255))

    # display images at different positions
    screen.blit(img_large, (0, 0))

    # update display
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
