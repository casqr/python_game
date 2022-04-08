# Import the important modules
import pygame
import os
import random

# initialize the pygame
pygame.init()

# set the display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("CATCH THE CLOWN")

# set the FPS
FPS = 60
clock = pygame.time.Clock()

# se the game values
PLAYER_STARTING_LIVE = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = 0.5

score = 0
player_lives = PLAYER_STARTING_LIVE

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

# set the colors
GREEN = (0, 255, 0)
YELLOW = (248, 231, 28)
BLUE = (0, 0, 255)

# set the fonts
font = pygame.font.Font(os.path.join('ASSETES', "SfCollegiate-K0Xe.ttf"), 32)

# set the text
title_text = font.render("Catch the Clown", True, GREEN)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render(f'SCORE: {score}', True, GREEN)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render(f'LIVES: {player_lives}', True, GREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render(f'GAME-OVER', True, YELLOW, BLUE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render(f'Press Mouse Button If You Wish to Continue', True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + game_over_rect.height*2)

# set the sound
click_sound = pygame.mixer.Sound(os.path.join('ASSETES', 'click_sound.wav'))
miss_sound = pygame.mixer.Sound(os.path.join('ASSETES', 'miss_s.wav'))
pygame.mixer.music.load(os.path.join('ASSETES', 'background_music.wav'))

# set the images
background_image = pygame.transform.scale(pygame.image.load(os.path.join('ASSETES', 'background_im.png')),
                                          (WINDOW_WIDTH, WINDOW_HEIGHT))
background_rect = background_image.get_rect()
background_rect.height = WINDOW_HEIGHT

clown_image = pygame.transform.scale(pygame.image.load(os.path.join('ASSETES', 'clown.png')), (65, 65))
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

laugh_image = pygame.transform.scale(pygame.image.load(os.path.join('ASSETES', 'laugh.png')), (65, 65))
laugh_rect = laugh_image.get_rect()
laugh_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# The main loop
pygame.mixer.music.play(-1, 0.0)
run = True
while run:
    # check the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # A click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            if clown_rect.collidepoint(mouse_x, mouse_y):
                print('click')
                click_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION

                # Move the clown in a new direction
                previous_dx = clown_dx
                previous_dy = clown_dy

                while previous_dx == clown_dx and previous_dy == clown_dy:
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])

            # We missed the clown
            else:
                WIN.blit(laugh_image, clown_rect)
                pygame.display.update()
                pygame.time.delay(100)
                miss_sound.play()
                player_lives -= 1

    # move the clown
    clown_rect.x += clown_dx * clown_velocity
    clown_rect.y += clown_dy * clown_velocity

    # Bounce the clown off the edges of the display
    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        clown_dx = -1 * clown_dx
    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy = -1 * clown_dy

    # update HUB
    score_text = font.render(f'SCORE: {score}', True, GREEN)
    lives_text = font.render(f'LIVES: {player_lives}', True, GREEN)

    # Chek for game over
    if player_lives == 0:
        WIN.blit(game_over_text, game_over_rect)
        WIN.blit(continue_text, continue_rect)
        pygame.display.update()

        # pause the game until the player clicks the rest button
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVE

                    clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                    clown_velocity = CLOWN_STARTING_VELOCITY
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])

                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False

                if event.type == pygame.QUIT:
                    pygame.quit()

    # Blit the background
    WIN.blit(background_image, background_rect)

    # Blit the HUB
    WIN.blit(title_text, title_rect)
    WIN.blit(score_text, score_rect)
    WIN.blit(lives_text, lives_rect)

    # Blit the assets
    WIN.blit(clown_image, clown_rect)

    # update the screen
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
