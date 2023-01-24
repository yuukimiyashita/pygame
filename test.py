import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("?")
clock = pygame.time.Clock()
testFont = pygame.font.Font("font/Pixeltype.ttf", 50)

skySurface = pygame.image.load("graphics/Sky.png").convert()
groundSurface = pygame.image.load("graphics/ground.png").convert()

scoreSurface = testFont.render("Who are you", True, "Black")
scoreRect = scoreSurface.get_rect(center = (400,50))


snailSurface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snailRect = snailSurface.get_rect(midbottom = (600,300))


playerSurface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
playerRect = playerSurface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface,(0,300))
    pygame.draw.rect(screen,"Pink", scoreRect)
    pygame.draw.rect(screen,"Pink", scoreRect, 10)
    screen.blit(scoreSurface,scoreRect)

    snailRect.left -= 4
    if snailRect.right <= 0: snailRect.left = 800
    screen.blit(snailSurface,snailRect)
    screen.blit(playerSurface,playerRect)

    

    pygame.display.update()
    clock.tick(60)