import sys
import threading
import pygame
import discord
from discord import app_commands
from discord.ext import commands

print("Hello!")

# --- DISCORD BOT ---

guildFile = open("guild.txt", "r")
guild_ID = guildFile.read()
guild = discord.Object(id=guild_ID)

intents = discord.Intents.default()
intents.message_content = True
class TFClient(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=intents)
        self.synced = False;
        
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = guild)
            self.synced = True
        print(f"We have logged in as {self.user}")

keyFile = open("key.txt", "r")
key = keyFile.read()

bot = TFClient()
tree = app_commands.CommandTree(bot)
    
def runBot():
    bot.run(key)
    
# --- PYGAME PART ---

class Enemy:
    currentLife = 0
    maxLife = 0
    def __init__(self, window) -> None:
        self.maxLife = int(input("Max enemy life: "))
        self.currentLife = self.maxLife
        self.enemySprite = pygame.image.load(input("Relative path to enemy sprite: "))
        self.enemyRect = self.enemySprite.get_rect()
        self.enemyPosition = width, height = 80, (window.windowSize[1]/2 - self.enemyRect.height/2)

    
class WindowProperties:
    windowSize = width, height = 1920, 1080
    windowWidth = windowSize[0]
    windowHeight = windowSize[1]
    healthSizeRatio = 720
    background = None
    screen = None
    
    def __init__(self) -> None:
        self.background = pygame.image.load(input("Relative path to background: "))
        self.screen = pygame.display.set_mode(self.windowSize)

pygame.init()

Window = WindowProperties()

DefaultEnemy = Enemy(Window)

def subtractLife(currentLife, damage):
    currentLife = currentLife - damage
    print(currentLife)
    return currentLife
    
@tree.command(name = "dmg", description= "Damage the enemy", guild = guild)
async def dmg(interaction: discord.Interaction, damage: int):
    DefaultEnemy.currentLife = DefaultEnemy.currentLife - damage
    await interaction.response.send_message(f"{damage} damage has been dealt to the enemy.")

@tree.command(name = "restart", description= "Restart the game given a set of parameters.", guild = guild)
async def restart(interaction: discord.Interaction, current_life: int, max_life: int):
    DefaultEnemy.maxLife = max_life
    DefaultEnemy.currentLife = current_life
    await interaction.response.send_message("Restarted game with given parameters")
    
threading.Thread(target=runBot, daemon=True).start()
    
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                DefaultEnemy.currentLife = subtractLife(DefaultEnemy.currentLife, 1)
                print(DefaultEnemy.currentLife/DefaultEnemy.maxLife)
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            
        Window.screen.blit(Window.background, (0, 0))
            
        # Draw our enemy
        Window.screen.blit(DefaultEnemy.enemySprite, DefaultEnemy.enemyPosition, DefaultEnemy.enemyRect)
            
            # draw our enemy's health bar
        healthBG = 40, 40, 40
        healthFG = 155, 0, 0
        pygame.draw.rect(Window.screen, healthBG, (Window.healthSizeRatio/2 + DefaultEnemy.enemyRect.width/1.5, (Window.windowSize[1]/2 - 48), Window.healthSizeRatio, Window.healthSizeRatio/7.5))
        pygame.draw.rect(Window.screen, healthFG, (Window.healthSizeRatio/2 + DefaultEnemy.enemyRect.width/1.5 + Window.healthSizeRatio/60, (Window.windowSize[1]/2 - Window.healthSizeRatio/20), (DefaultEnemy.currentLife/DefaultEnemy.maxLife) * (Window.healthSizeRatio - Window.healthSizeRatio/30), 72))
            
        pygame.display.flip()