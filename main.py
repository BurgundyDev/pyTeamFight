import asyncio
import sys
import threading
import pygame
import discord
from discord.ext import commands

print("Hello!")

# --- DISCORD BOT ---

keyFile = open("key.txt", "r")
key = keyFile.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
    
# --- PYGAME PART ---

class Enemy:
    currentLife = 0
    maxLife = 0
    enemySprite = None
    enemyRect = None
    enemyPosition = None

class WindowProperties:
    windowSize = width, height = 1920, 1080
    windowWidth = windowSize[0]
    windowHeight = windowSize[1]
    healthSizeRatio = 720
    background = None
    screen = None
    
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(self.windowSize)

DefaultEnemy = Enemy()

Window = WindowProperties()

pygame.init()

def renderFight(enemy, window):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                enemy.currentLife = subtractLife(enemy.currentLife, 1)
                print(enemy.currentLife/enemy.maxLife)
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            
        window.screen.blit(window.background, (0, 0))
            
        # Draw our enemy
        window.screen.blit(enemy.enemySprite, enemy.enemyPosition, enemy.enemyRect)
            
            # draw our enemy's health bar
        healthBG = 40, 40, 40
        healthFG = 155, 0, 0
        pygame.draw.rect(window.screen, healthBG, (window.healthSizeRatio/2 + enemy.enemyRect.width/1.5, (window.windowSize[1]/2 - 48), window.healthSizeRatio, window.healthSizeRatio/7.5))
        pygame.draw.rect(window.screen, healthFG, (window.healthSizeRatio/2 + enemy.enemyRect.width/1.5 + window.healthSizeRatio/60, (window.windowSize[1]/2 - window.healthSizeRatio/20), (enemy.currentLife/enemy.maxLife) * (window.healthSizeRatio - window.healthSizeRatio/30), 72))
            
        pygame.display.flip()

def subtractLife(currentLife, damage):
    currentLife = currentLife - damage
    print(currentLife)
    return currentLife  

@bot.event
async def on_ready():
    print('Bot is ready!')

@bot.command(name = "start", help = "Starts the bot on the server")
async def starter(ctx):
    loop = bot.loop
    
    DefaultEnemy.maxLife = int(input("Type max amount of enemy life: "))

    DefaultEnemy.currentLife = DefaultEnemy.maxLife

    # Set of variables for enemy object
    # enemySprite = pygame.image.load("intro_ball.gif")
    DefaultEnemy.enemySprite = pygame.image.load(input("Type relative path to enemy sprite: "))
    DefaultEnemy.enemyRect = DefaultEnemy.enemySprite.get_rect()
    DefaultEnemy.enemyPosition = width, height = 80, (Window.windowSize[1]/2 - DefaultEnemy.enemyRect.height/2)

    Window.background = pygame.image.load(input("Type relative path to background: "))
    renderFight(DefaultEnemy, Window)

    
            
@bot.command(name="damage", help = "Damages the enemy.")
async def damage(ctx, arg):
    DefaultEnemy.currentLife = DefaultEnemy.currentLife - int(arg)
    renderFight(DefaultEnemy, Window)
    await ctx.send("Enemy's current life is: " + str(DefaultEnemy.currentLife))

bot.run(key)