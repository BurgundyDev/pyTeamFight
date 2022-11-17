# pyTeamFight
Simple Discord bot to have a big battle against a boss enemy with Your friends.

Made for a party, this bot simultanously launches a pygame window and a Discord bot. The pygame window shows a boss sprite as well as an health bar, which can be controlled using Discord bot commands.

## Usage

1. Download dependencies (requires Python to be installed and added to PATH)
```
pip install pygame
pip install discord.py
```

2. Clone the repo 
```
git clone https://github.com/BurgundyDev/pyTeamFight
cd pyTeamFight
```

3. Add ``key.txt`` (containing Your Discord bot token) and  ``guild.txt`` (containing the ID of Your server), as well as two images - one containing the boss enemy, other containing the background image (preferably 1920x1080)

4. Invite the Discord bot You've created to the server.

5. Run ``main.py`` and type in Your enemy's max HP and relative paths of the background and boss images, as instructed,

Now You are all set and done. You can deal damage with the ``/dmg`` command and restart the boss with desired current and max HP with the ``/restart`` command.
