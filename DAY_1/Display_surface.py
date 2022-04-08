import pygame

# Initialize pygame
pygame.init()

# Set the screen height and width variable
WIDTH = 900
HEIGHT = 600

# set the screen size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First pygame')  # set the title of the window


def main():
    run = True
    while run:
        for event in pygame.event.get():  # check in the events
            if event.type == pygame.QUIT:  # if the events is quit
                run = False  # Then we turn off the while loop

    pygame.quit()  # And then we quit the pygame environment


if __name__ == '__main__':
    main()
