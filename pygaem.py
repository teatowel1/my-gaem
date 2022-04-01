import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True

sky_surface = pygame.image.load('Code\Graphics/s1.png').convert_alpha()
ground_surface = pygame.image.load('Code\Graphics/g4.png').convert_alpha()

game_over_text_surface = test_font.render('Game over. Press space to try again.', False, 'Black')
game_over_text_rect = game_over_text_surface.get_rect(midtop=(400, 50))

text_surface = test_font.render('e', False, 'Black')
text_rect = text_surface.get_rect(midleft=(10, 50))

snail_surface = pygame.image.load('Code\Graphics/c32.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 303))

player_surf = pygame.image.load('Code\Graphics/harold_walking.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 270))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(1)
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
               if player_rect.collidepoint(event.pos):
                   player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800



    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, 'Light Blue', text_rect)
        screen.blit(text_surface, text_rect)

        snail_rect.x -= 5.5
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if snail_rect.colliderect(player_rect):
          game_active = False
    else:
        screen.fill('Blue')
        screen.blit(game_over_text_surface, game_over_text_rect)
    pygame.display.update()

    clock.tick(90)
