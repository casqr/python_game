import pygame

pygame.init()

# VARIABLE FOR WIDTH AND HEIGHT
WIDTH = 900
HEIGHT = 600

# set the window height, width and the caption
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adding Image")

# set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


# define the drawing function
def drawing(win):
    win.fill(WHITE)
    pygame.draw.line(win, BLACK, (0, 0), (WIDTH, HEIGHT), 10)
    pygame.draw.line(win, BLACK, (WIDTH // 2, HEIGHT // 2), (WIDTH // 2, HEIGHT), 10)
    pygame.draw.circle(win, GREEN, (WIDTH // 2, HEIGHT // 2), 200, 30)
    pygame.draw.rect(win, BLACK, (500, 300, 200, 200), 30)
    pygame.display.update()


# DEFINE THE MAIN FUNCTION
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawing(WIN)

    pygame.quit()


if __name__ == '__main__':
    main()
