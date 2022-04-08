import pygame, sys, math

pygame.init()

FPS = 60  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Projectile Motion')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

delta_t = 0.01
m = 1
g = 9.8

fx = 0
fy = m * g

x = 0
y = 0

vx = 50
vy = 0

while True:

    vx = vx + (fx / m) * delta_t
    vy = vy + (fy / m) * delta_t

    x = x + vx * delta_t
    y = y + vy * delta_t

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.update()
    fpsClock.tick(FPS)
