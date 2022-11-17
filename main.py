import sys
import pygame
import discord

print("Hello!")

def subtractLife(currentLife, damage):
    currentLife = currentLife - damage
    print(currentLife)
    return currentLife  

pygame.init()
windowSize = width, height = 1280, 720

currentLife = 0
# maxLife = 100
maxLife = int(input("Type max amount of enemy life: "))

currentLife = maxLife

lifeFont = pygame.font.SysFont("Verdana", 50, False, False)

black = 0, 0, 0, 155

# Set of variables for enemy object
# enemySprite = pygame.image.load("intro_ball.gif")
enemySprite = pygame.image.load(input("Type relative path to enemy sprite: "))
enemyRect = enemySprite.get_rect()
enemyPosition = width, height = 200, (windowSize[1]/2 - enemyRect.height/2)

screen = pygame.display.set_mode(windowSize)

while currentLife > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                currentLife = subtractLife(currentLife, 1)
                print(currentLife/maxLife)
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    
    screen.fill(black)
    
    # Draw our enemy
    screen.blit(enemySprite, enemyPosition, enemyRect)
    
    # draw our enemy's health bar
    healthBG = 40, 40, 40
    healthFG = 255, 0, 120
    pygame.draw.rect(screen, healthBG, (400+enemyRect.width, (windowSize[1]/2 - 40), 600, 80))
    pygame.draw.rect(screen, healthFG, (400+enemyRect.width + 10, (windowSize[1]/2 - 30), (currentLife/maxLife) * 580, 60))
    
    pygame.display.flip()