import pygame
import math

pygame.init()

# SET THE GAME SIZE
WIDTH, HEIGHT = (900, 500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Having Fun with maths")

# set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


def draw(x, y):
    WIN.fill(BLACK)
    pygame.draw.circle(WIN, GREEN, (x, y), 10)
    pygame.display.update()


def trigonometry(angle, radius):
    # A little bit of review for trig
    """
    To find the x and y of a trigonometric function we use SOHCAHTOA
    x = R*Cos(angle)
    y = R*Sin(angle)
    """
    x = int(radius * math.cos(angle) + WIDTH // 2)
    y = int(radius * math.sin(angle) + HEIGHT // 2)
    return [x, y]


# set frame FPS
FPS = 5
clock = pygame.time.Clock()


# set the game loop
def main():
    angle = 0
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # for the circular motion circle
        dx, dy = trigonometry(angle, 200)

        draw(dx, dy)
        angle += 0.5

    pygame.quit()


if __name__ == '__main__':
    main()
