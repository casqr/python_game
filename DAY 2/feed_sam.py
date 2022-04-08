import pygame
import os
import random

# initialize the game
pygame.init()

# set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Feed SAM')

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# set the game value
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# set the colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set fonts
font = pygame.font.SysFont("microsofthimalaya", 32)

# set text
score_text = font.render("score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed Sam", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = game_over_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2 - continue_rect.width//2, WINDOW_HEIGHT // 2 + 32)

# set sound
coin_sound = pygame.mixer.Sound(os.path.join('ASSET', 'sound_for_coin.wav'))
pygame.mixer.music.load(os.path.join('ASSET', 'background_sound.wav'))

# set the images
player_image = pygame.transform.flip(pygame.image.load(os.path.join('ASSET', 'dragon-face.png')), True, False)
#player_image = pygame.transform.scale(pygame.image.load(os.path.join('ASSET', 'sam_1.jpg')), (71,71))
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2

coin_image = pygame.transform.scale(pygame.image.load(os.path.join('ASSET', 'coin-icon.png')), (30, 30))
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)


# drawing function
def drawing(score_text, lives_text):
    global score
    global player_lives, coin_velocity
    # blit the hub to the screen
    display_surface.fill(BLACK)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0, 64), (WINDOW_WIDTH, 64))

    # blit the assets to the screen
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)

    # check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        # pause the game until player presses a key, then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT // 2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    run = False

    pygame.display.update()


# The main game loop
def main():
    global score
    global player_lives, coin_velocity

    pygame.mixer.music.play(-1, 0.0)
    run = True
    while run:
        # check to see if user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # check to see if the user wants to move
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and player_rect.top > 64:
            player_rect.y -= PLAYER_VELOCITY
        if key[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
            player_rect.y += PLAYER_VELOCITY

        # Move the coin
        if coin_rect.x < 0:
            # Player missed the coin
            player_lives -= 1
            coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
            coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
        else:
            coin_rect.x -= coin_velocity
        if player_rect.colliderect(coin_rect):
            score += 1
            coin_sound.play()
            coin_velocity += COIN_ACCELERATION
            coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
            coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
        # update the HUB
        score_text = font.render(f'Score: {score}', True, GREEN, DARKGREEN)
        lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)

        drawing(score_text, lives_text)
        clock.tick(FPS)

    # End the game
    pygame.quit()


if __name__ == '__main__':
    main()
