import pygame
import os

# initialize fonts
pygame.font.init()
pygame.init()  # initialize pygame

# set the width and height variable
WIDTH = 900
HEIGHT = 600

# set fonts
FONT = pygame.font.SysFont('calibri', 50)
# set the screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blitting an image')

# Loading the image 
my_image_1 = pygame.image.load(os.path.join('ASSETS', 'cante-ASSET.jpg'))
my_im_rect = my_image_1.get_rect()
my_im_rect.topright = (WIDTH, 0)

# Loading the image 2
my_image_2 = pygame.image.load(os.path.join('ASSETS', 'cante-ASSET.jpg'))
my_im_rect_2 = my_image_2.get_rect()
my_im_rect_2.center = (WIDTH // 2, HEIGHT // 2)

# Loading the image 3
my_image_3 = pygame.image.load(os.path.join('ASSETS', 'cante-ASSET.jpg'))
my_im_rect_3 = my_image_3.get_rect()
my_im_rect_3.bottomleft = (0, HEIGHT)

# set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# then we render the text
text = FONT.render("My name is cante", True, BLUE)
text_rec = text.get_rect()
text_rec.center = (WIDTH // 2, HEIGHT // 2)


# create a drawing function
def drawing():
    WIN.fill(BLACK)
    WIN.blit(my_image_1, my_im_rect)
    WIN.blit(my_image_2, my_im_rect_2)
    WIN.blit(my_image_3, my_im_rect_3)
    WIN.blit(text, text_rec)

    pygame.display.update()


# create a main function
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawing()

    pygame.quit()


if __name__ == '__main__':
    main()
