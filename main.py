import sys
import threading
import pygame
import discord

print("Hello!")

# --- DISCORD BOT ---

keyFile = open("key.txt", "r")
key = keyFile.read()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
    
# --- PYGAME PART ---

def subtractLife(currentLife, damage):
    currentLife = currentLife - damage
    print(currentLife)
    return currentLife  

@client.event
async def on_ready():
    pygame.init()
    windowSize = width, height = 1920, 1080
    windowWidth = windowSize[0]
    windowHeight = windowSize[1]

    healthSizeRatio = 720

    currentLife = 0
    maxLife = int(input("Type max amount of enemy life: "))

    currentLife = maxLife

    lifeFont = pygame.font.SysFont("Verdana", 50, False, False)

    black = 0, 0, 0

    # Set of variables for enemy object
    # enemySprite = pygame.image.load("intro_ball.gif")
    enemySprite = pygame.image.load(input("Type relative path to enemy sprite: "))
    enemyRect = enemySprite.get_rect()
    enemyPosition = width, height = 80, (windowSize[1]/2 - enemyRect.height/2)

    background = pygame.image.load(input("Type relative path to background: "))

    screen = pygame.display.set_mode(windowSize)
    
    while currentLife > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        currentLife = subtractLife(currentLife, 1)
                        print(currentLife/maxLife)
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            
            screen.fill(black)
            screen.blit(background, (0, 0))
            
            # Draw our enemy
            screen.blit(enemySprite, enemyPosition, enemyRect)
            
            # draw our enemy's health bar
            healthBG = 40, 40, 40
            healthFG = 155, 0, 0
            pygame.draw.rect(screen, healthBG, (healthSizeRatio/2 + enemyRect.width/1.5, (windowSize[1]/2 - 48), healthSizeRatio, healthSizeRatio/7.5))
            pygame.draw.rect(screen, healthFG, (healthSizeRatio/2 + enemyRect.width/1.5 + healthSizeRatio/60, (windowSize[1]/2 - healthSizeRatio/20), (currentLife/maxLife) * (healthSizeRatio - healthSizeRatio/30), 72))
            
            pygame.display.flip()
            
client.run(key)