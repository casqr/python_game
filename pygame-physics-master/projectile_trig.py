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

    pygame.draw.circle(WIN, GREEN, (x, y), 10)
    WIN.fill(BLACK)
    pygame.display.update()


def trigonometry(angle, speedx, speedy):
    # A little bit of review for trig
    """
    To find the x and y of a trigonometric function we use SOHCAHTOA
    x = R*Cos(angle)
    y = R*Sin(angle)
    """
    m = 1
    g = 9.8

    fx = 0
    fy = m * g

    theta = math.radians(angle)

    vx = speedx * math.cos(theta)
    vy = -speedy * math.sin(theta)

    t = 0.01
    vx = vx + (fx / m) * t
    vy = vy + (fy / m) * t

    x = vx * t
    y = vy * t
    return [x, y]


# set frame FPS
FPS = 60
clock = pygame.time.Clock()


# set the game loop
def main():
    speed = 100
    angle = 45
    dx, dy = trigonometry(angle, speed, speed)
    x, y = (0, HEIGHT)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # for the circular motion circle
        x += dx
        y += dy

        if x < 0 or x > WIDTH:
            dx = -dx
            speed -= 2
        if y < 0 or y > HEIGHT:
            dy = -dy
            speed -= 1

        draw(x, y)
        # angle += 0.5

    pygame.quit()


if __name__ == '__main__':
    main()
