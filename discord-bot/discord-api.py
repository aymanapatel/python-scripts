import os 

import discord

from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

print(DISCORD_TOKEN)

client = discord.Client()
# GUILD = "Welcome to Life"

@client.event
async def on_ready():
    
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        # print('Response')
        await message.channel.send('Hello!')

    if message.content.startswith('group'):
        for guild in client.guilds:
            response = "Guild name: " +  guild.name +  "Guild id: " +  str(guild.id)
            await message.channel.send(response) 

        

client.run(DISCORD_TOKEN)
