# import the pygame library
import pygame
import os

# set the width and height
WIDTH = 900
HEIGHT = 700

# SET THE DISPLAY
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Continuous value")

# load the image
im = pygame.image.load(os.path.join('ASSETS', 'cante-ASSET.jpg'))
im_rect = im.get_rect()
im_rect.topleft = (0, 0)

# load another image
im_2 = pygame.image.load(os.path.join('ASSETS', 'cante-ASSET.jpg'))
im_rect_2 = im.get_rect()
im_rect_2.topright = (WIDTH, 0)

# set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


# make the drawing function
def drawing():
    WIN.fill(BLACK)
    WIN.blit(im, im_rect)
    WIN.blit(im_2, im_rect_2)
    pygame.display.update()


# set the FPS
FPS = 60


# make the main function
def main():
    # set the clock so we can run the FPS
    clock = pygame.time.Clock()
    vel = 5
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                run = False
        drawing()
        # set the continuous button
        button = pygame.key.get_pressed()
        if button[pygame.K_UP] and im_rect.top > 0:
            im_rect.y -= vel
        elif button[pygame.K_DOWN] and im_rect.bottom < HEIGHT:
            im_rect.y += vel
        elif button[pygame.K_LEFT] and im_rect.left > 0:
            im_rect.x -= vel
        elif button[pygame.K_RIGHT] and im_rect.right < WIDTH:
            im_rect.x += vel
        if im_rect.colliderect(im_rect_2):
            im_rect_2.x -= vel
            print('HIT')

    pygame.quit()


if __name__ == '__main__':
    main()
