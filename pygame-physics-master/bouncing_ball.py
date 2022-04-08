import pygame

pygame.init()

# SET THE GAME SIZE
WIDTH, HEIGHT = (900, 500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Having Fun with maths")

# set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Load the laughing emoji
laugh = pygame.image.load('laugh.png')
laugh_rect = laugh.get_rect()
laugh_rect.center = (WIDTH // 2, HEIGHT // 2)


def draw(x, y):
    WIN.fill(BLACK)
    pygame.draw.circle(WIN, GREEN, (x, y), 10)
    WIN.blit(laugh, laugh_rect)
    pygame.display.update()


# set frame FPS
FPS = 144
clock = pygame.time.Clock()


# set the game loop
def main():
    x, y = (0, 0)
    dx = 1
    dy = 1

    tx = 1
    ty = 1
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # for the bouncing circle
        x += dx
        y += dy

        # for the laughing emoji
        laugh_rect.x += tx
        laugh_rect.y += ty

        if x < 0 or x > WIDTH:
            dx = -dx
        elif y < 0 or y > HEIGHT:
            dy = -dy

        if laugh_rect.x < 0 or laugh_rect.x > WIDTH - 50:
            tx = -tx
        elif laugh_rect.y < 0 or laugh_rect.y > HEIGHT - 50:
            ty = -ty

        draw(x, y)

    pygame.quit()


if __name__ == '__main__':
    main()
