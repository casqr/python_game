# Today we are going to be making the snake game
import pygame
import random

# Initialize pygame
pygame.init()

# Set the boundaries
WIN_WIDTH = 600
WIN_HEIGHT = 600

# set the display
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('~~snake~~')

# set the clock
FPS = 60
clock = pygame.time.Clock()

# set the game values
SNAKE_SIZE = 30

head_x = WIN_WIDTH // 2
head_y = WIN_HEIGHT // 2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARK_RED = (150, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set fonts
font = pygame.font.SysFont('gabriola', 30)

# set text
title_text = font.render("~~SNAKE-GAME~~", True, GREEN, DARK_RED)
title_rect = title_text.get_rect()
title_rect.center = (WIN_WIDTH // 2, 30)

score_text = font.render("Score: " + str(score), True, GREEN, DARK_RED)
score_rect = title_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAME-OVER", True, GREEN, DARK_RED)
game_over_rect = title_text.get_rect()
game_over_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)

continue_text = font.render(f'Press Any Button If You Wish to Continue', True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + game_over_rect.height * 2)

# set sound
pick_sound = pygame.mixer.Sound("sound_for_coin.wav")

# set images (using simple rect)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(WIN, RED, apple_coord)
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(WIN, GREEN, head_coord)
body_cord = []

# set the game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # move the snake
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1 * SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # Add the head coordinate in the first index of the body
    body_cord.insert(0, head_coord)
    body_cord.pop()
    # Update the x and y position coordinate
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    # check for game over
    if head_rect.left < 0 or head_rect.right > WIN_WIDTH or head_rect.top < 0 or head_rect.bottom > WIN_HEIGHT or head_coord in body_cord:
        WIN.blit(game_over_text, game_over_rect)
        WIN.blit(continue_text, continue_rect)
        pygame.display.update()

        # pause the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    head_x = WIN_WIDTH//2
                    head_y = WIN_HEIGHT//2 + 100
                    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
                    body_cord = []
                    snake_dx = 0
                    snake_dy = 0
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    run = False

    # check for collisions
    if head_rect.colliderect(apple_rect) and apple_rect.width < score_rect.bottom:
        score += 1
        pick_sound.play()
        apple_x = random.randint(0, WIN_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WIN_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

        # Add to the body
        body_cord.append(head_coord)

    # Update the HUD
    score_text = font.render("Score: " + str(score), True, GREEN, DARK_RED)

    WIN.fill(BLACK)
    # Blit the HUD
    WIN.blit(title_text, title_rect)
    WIN.blit(score_text, score_rect)

    # blit the assets
    for body in body_cord:
        pygame.draw.rect(WIN, GREEN, body)
    head_rect = pygame.draw.rect(WIN, GREEN, head_coord)
    apple_rect = pygame.draw.rect(WIN, RED, apple_coord)

    # Update the display
    pygame.display.update()
    clock.tick(20)

pygame.quit()
