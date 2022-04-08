import pygame
import os

# initialize fonts
pygame.font.init()
pygame.init()  # initialize pygame

# set the width and height variable
WIDTH = 900
HEIGHT = 600

# set the screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blitting an image')

# Loading the image
my_image_1 = pygame.image.load(os.path.join('ASSETS', 'cante-ASSET.jpg'))
my_im_rect = my_image_1.get_rect()
my_im_rect.topright = (WIDTH, 0)


# set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# create a drawing function
def drawing():
    WIN.fill(BLACK)
    WIN.blit(my_image_1, my_im_rect)

    pygame.display.update()


# create a main function
def main():
    vel = 5
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # check whether or not THE MOUSE is being pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                my_im_rect.centery = mouse_y
                my_im_rect.centerx = mouse_x
            # check for the mouse motion
            elif event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                my_im_rect.centery = mouse_y
                my_im_rect.centerx = mouse_x

        drawing()

    pygame.quit()


if __name__ == '__main__':
    main()